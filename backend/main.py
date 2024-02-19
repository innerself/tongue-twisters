from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from .app.api import router
from .app.config import TORTOISE_SETTINGS

app = FastAPI()

register_tortoise(app, config=TORTOISE_SETTINGS)
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888)
