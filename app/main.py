from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.settings import settings


app = FastAPI(
    title=settings.APP_NAME,
    description="we are the champions",
)
templates = Jinja2Templates(directory=Path(__file__).parent.parent / 'templates')


@app.get('/mkdocs')
async def documentation():
    pass


@app.get('/')
def greetings(request: Request, message: str = 'HELLO WORLD!'):
    context = {
        "title": message,
        "request": request,
    }
    response = templates.TemplateResponse('base.html', context=context)
    return response


if __name__ == "__main__":  # pragma: no cover
    # useful for debug mode
    import uvicorn

    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8001)  # pragma: no cover
