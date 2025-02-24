from starlette.applications import Starlette
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src import configs


templates = Jinja2Templates(directory='src/templates')


async def index(request):
    return templates.TemplateResponse('index.html', {'request': request})


async def about_me(request):
    return templates.TemplateResponse('about_me.html', {'request': request})


app = Starlette(
    routes=[
        Route('/', index),
        Route('/about_me', about_me),
    ],
    debug=configs.DEV,
)

app.mount('/static', StaticFiles(directory='src/static'), name='static')
