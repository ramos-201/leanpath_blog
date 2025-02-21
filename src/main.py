from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from src import config


async def index(request):
    return JSONResponse({'message': 'Hello, World!'})


app = Starlette(
    routes=[
        Route('/', index),
    ],
    debug=config.DEV,
)
