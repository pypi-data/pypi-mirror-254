from enum import Enum
from typing import List
from fastapi.responses import JSONResponse
from ..di import DIContainer
from ..routing import Registry
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.routing import APIRoute, BaseRoute
from fastapi.middleware.cors import CORSMiddleware


class APIController:
    routes = []

    def __init__(self,
                 app: FastAPI,
                 cors_origins: List[str]=None,
                 generate_options_endpoints: bool=True,
                 generate_head_endpoints: bool=True,
                 debug_mode: bool=False
                 ) -> None:
        self.__app = app        
        self.__generate_options_endpoints = generate_options_endpoints
        self.__generate_head_endpoints = generate_head_endpoints   
        self.__debug_mode = debug_mode     
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

        self.__add_exception_handlers()

    def __add_route(self, bound_method: callable, method: Enum, path: str) -> None:
        self.__app.add_api_route(
            path=path,
            endpoint=bound_method,
            methods=[method.value]
        )
        if method.value == 'GET' and self.__generate_head_endpoints:
            self.__add_head(path)

    def __add_head(self, path: str) -> None:
        self.__app.add_api_route(
            path=path,
            endpoint=self.__head_handler,
            methods=['HEAD']
        )

    def __add_cors(self, cors_origins: List[str]) -> None:
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

    def __add_exception_handlers(self) -> None:
        self.__app.add_exception_handler(400, self.bad_request)
        self.__app.add_exception_handler(401, self.not_authorized)
        self.__app.add_exception_handler(403, self.forbidden)
        self.__app.add_exception_handler(404, self.not_found)
        self.__app.add_exception_handler(405, self.method_not_allowed)
        self.__app.add_exception_handler(500, self.internal_server_error)

    def bad_request(self,  request: Request, exc: HTTPException) -> JSONResponse:
        path = request.url.path
        method = request.method
        content = {"detail": f"Bad Request for method {method} and path {path}"}
        if self.__debug_mode:
            content["exception"] = exc.detail
        return JSONResponse(status_code=400, content=content)
    
    def not_authorized(self,  request: Request, exc: HTTPException) -> JSONResponse:
        path = request.url.path
        method = request.method
        content = {"detail": f"Not authorized for method {method} and path {path}"}
        if self.__debug_mode:
            content["exception"] = exc.detail
        return JSONResponse(status_code=401, content=content)
    
    def forbidden(self, request: Request, exc: HTTPException) -> JSONResponse:
        path = request.url.path
        method = request.method
        content = {"detail": f"Forbidden for method {method} and path {path}"}
        if self.__debug_mode:
            content["exception"] = exc.detail
        return JSONResponse(status_code=403, content=content)

    def not_found(self, request: Request, exc: HTTPException) -> JSONResponse:
        path = request.url.path        
        content = {"detail": f"Path {path} not found"}
        if self.__debug_mode:
            content["exception"] = exc.detail
        return JSONResponse(status_code=404, content=content)
    
    def method_not_allowed(self, request: Request, exc: HTTPException) -> JSONResponse:
        path = request.url.path
        method = request.method
        content = {"detail": f"Method {method} not allowed path {path}"}
        if self.__debug_mode:
            content["exception"] = exc.detail
        return JSONResponse(status_code=405, content=content)
    
    def internal_server_error(self, request: Request, exc: HTTPException) -> JSONResponse:
        path = request.url.path
        method = request.method
        content = {"detail": f"Internal server error for method {method} and path {path}"}
        if self.__debug_mode:
            content["exception"] = exc.detail
        return JSONResponse(status_code=403, content=content)   
    
    @staticmethod
    def __get_methods_for_route(route: APIRoute, current_routes: List[BaseRoute]) -> List[str]:
        methods = set()
        for r in current_routes:
            if isinstance(r, APIRoute) and r.path == route.path:
                methods.update(r.methods)
        return list(methods)

    @staticmethod
    async def __head_handler() -> Response:
        return Response()
