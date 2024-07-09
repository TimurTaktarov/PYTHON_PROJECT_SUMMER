from fastapi import FastAPI
from app.settings import settings


app = FastAPI(
    title=settings.APP_NAME,
    description="we are the champions",
)


@app.get('/mkdocs')
async def documentation(message):
    pass



if __name__ == "__main__":  # pragma: no cover
    # useful for debug mode
    import uvicorn

    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8001)  # pragma: no cover
