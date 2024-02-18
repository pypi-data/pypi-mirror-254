# Web API Controllers

## Description
Simple Web API controller framework for FastAPI

## Installation

To install this package, use pip:

```bash
pip install webapicontrollers
```

## Example
```python
from fastapi import FastAPI
from webapicontrollers import APIController, Get, Post, Patch, Delete, Put, RoutePrefix

@RoutePrefix('/test')
class TestController(APIController):

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    @Get('/')
    async def get(self) -> dict:
        return {"method": "GET", "path": "/"}

    @Get('/{arg}')
    async def get_with_arg(self, arg) -> dict:
        return {"method": "GET", "path": "/", "arg": arg}

    @Post('/')
    async def post(self) -> dict:
        return {"method": "POST", "path": "/"}

    @Post('/{arg}')
    async def post_with_arg(self, arg) -> dict:
        return {"method": "POST", "path": "/", "arg": arg}
    
    @Put('/')
    async def put(self) -> dict:
        return {"method": "PUT", "path": "/"}
    
    @Put('/{arg}')
    async def put_with_arg(self, arg) -> dict:
        return {"method": "PUT", "path": "/", "arg": arg}
    
    @Patch('/')
    async def patch(self) -> dict:
        return {"method": "PATCH", "path": "/"}
    
    @Patch('/{arg}')
    async def patch_with_arg(self, arg) -> dict:
        return {"method": "PATCH", "path": "/", "arg": arg}
    
    @Delete('/')
    async def delete(self) -> dict:
        return {"method": "DELETE", "path": "/"}
    
    @Delete('/{arg}')
    async def delete_with_arg(self, arg) -> dict:
        return {"method": "DELETE", "path": "/", "arg": arg}


app = FastAPI()
test_controller = TestController(app)
```
## Caution
This project is in a very early state and might not be very useful to anyone yet. There is no support avilable, use at your own risk.

## License

This project is licensed under the [MIT License](LICENSE).
