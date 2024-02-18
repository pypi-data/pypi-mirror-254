from typing import List

from fastapi.responses import JSONResponse
from ..di import DIContainer
from ..routing import Registry
from fastapi import FastAPI, Response
from fastapi.routing import APIRoute, BaseRoute
from fastapi.middleware.cors import CORSMiddleware


class APIController:
    routes = []

    def __init__(self,
                 app: FastAPI,
                 cors_origins: List[str]=None,
                 generate_options_endpoints: bool=True,
                 generate_head_endpoints: bool=True
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

    def __add_route(self, bound_method, method, path) -> None:
        self.__app.add_api_route(
            path=path,
            endpoint=bound_method,
            methods=[method.value]
        )
        if method.value == 'GET' and self.__generate_head_endpoints:
            self.__add_head(path)

    def __add_head(self, path) -> None:
        self.__app.add_api_route(
            path=path,
            endpoint=self.__head_handler,
            methods=['HEAD']
        )

    def __add_cors(self, cors_origins) -> None:
        # noinspection PyTypeChecker
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=cors_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __add_options_endpoints(self) -> None:
        current_routes = self.__app.routes.copy()
        for route in current_routes:
            if isinstance(route, APIRoute):
                self.__add_options_route(route, current_routes)

    def __add_options_route(self, route: APIRoute, current_routes: List[BaseRoute]) -> None:
        methods = self.__get_methods_for_route(route, current_routes)
        # noinspection PyTypeChecker
        self.__app.add_api_route(
            path=route.path,
            endpoint=lambda: {"allowed_methods": methods},
            methods=["OPTIONS"],
        )

    def not_found(self, path: str) -> JSONResponse:
        return JSONResponse(status_code=404, content={"message": f"Path {path} not found"})
    
    def method_not_allowed(self, path: str, method: str) -> JSONResponse:
        return JSONResponse(status_code=405, content={"message": f"Method {method} not allowed for path {path}"})
    
    def server_error(self, path: str, method: str, error: str) -> JSONResponse:
        return JSONResponse(status_code=500, content={"message": f"Error {error} for method {method} and path {path}"})
    
    def bad_request(self, path: str, method: str, error: str) -> JSONResponse:
        return JSONResponse(status_code=400, content={"message": f"Error {error} for method {method} and path {path}"})
    
    def not_authorized(self, path: str, method: str, error: str) -> JSONResponse:
        return JSONResponse(status_code=401, content={"message": f"Error {error} for method {method} and path {path}"})
    
    def forbidden(self, path: str, method: str, error: str) -> JSONResponse:
        return JSONResponse(status_code=403, content={"message": f"Error {error} for method {method} and path {path}"})

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
