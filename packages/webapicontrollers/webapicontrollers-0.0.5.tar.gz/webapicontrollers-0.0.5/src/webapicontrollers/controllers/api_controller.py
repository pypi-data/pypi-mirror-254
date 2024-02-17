from typing import List
from ..di import DIContainer
from ..routing import Registry
from fastapi import FastAPI, Response
from fastapi.routing import APIRoute, BaseRoute
from fastapi.middleware.cors import CORSMiddleware


class APIController:
    routes = []

    def __init__(self,
                 app: FastAPI,
                 cors_origins=None,
                 generate_options_endpoints=True,
                 generate_head_endpoints=True
                 ) -> None:
        self.__app = app        
        self.__generate_options_endpoints = generate_options_endpoints
        self.__generate_head_endpoints = generate_head_endpoints        
        if cors_origins is not None:
            self.__add_cors(cors_origins)

        self.__register_routes()

    def __register_routes(self) -> None:
        container = DIContainer(Registry())
        registry = container.get(Registry)
        self.__routes = registry.get_routes()

        for func, path, method in self.__routes:
            if hasattr(self,'_route_prefix'):
                path = self._route_prefix + path
                
            if hasattr(self, func.__name__) and callable(getattr(self, func.__name__)):
                bound_method = getattr(self, func.__name__)            
                self.__add_route(bound_method, method, path)

        if self.__generate_options_endpoints:
            self.__add_options_endpoints()

    def __add_route(self, bound_method, method, path):
        self.__app.add_api_route(
            path=path,
            endpoint=bound_method,
            methods=[method.value]
        )
        if method.value == 'GET' and self.__generate_head_endpoints:
            self.__add_head(path)

    def __add_head(self, path):
        self.__app.add_api_route(
            path=path,
            endpoint=self.__head_handler,
            methods=['HEAD']
        )

    def __add_cors(self, cors_origins):
        # noinspection PyTypeChecker
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=cors_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __add_options_endpoints(self):
        current_routes = self.__app.routes.copy()
        for route in current_routes:
            if isinstance(route, APIRoute):
                self.__add_options_route(route, current_routes)

    def __add_options_route(self, route: APIRoute, current_routes: List[BaseRoute]):
        methods = self.__get_methods_for_route(route, current_routes)
        # noinspection PyTypeChecker
        self.__app.add_api_route(
            path=route.path,
            endpoint=lambda: {"allowed_methods": methods},
            methods=["OPTIONS"],
        )

    @staticmethod
    def __get_methods_for_route(route: APIRoute, current_routes) -> List[str]:
        methods = set()
        for r in current_routes:
            if isinstance(r, APIRoute) and r.path == route.path:
                methods.update(r.methods)
        return list(methods)

    @staticmethod
    async def __head_handler() -> Response:
        return Response()
