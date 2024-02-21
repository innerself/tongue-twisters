from pathlib import Path

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise

from .app.api import router
from .app.config import TORTOISE_SETTINGS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.mount("/static", StaticFiles(directory=Path('frontend/build'), html=True), name="static")

register_tortoise(app, config=TORTOISE_SETTINGS)
app.include_router(router, prefix='/api')


@app.get("/")
async def app_root():
    return FileResponse(Path('frontend/build/index.html'))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888)
