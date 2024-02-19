from fastapi import APIRouter, HTTPException

from . import schemas, service

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get('/twisters/')
async def get_twisters_list() -> list[schemas.Twister]:
    return await service.get_all_twisters()


@router.post('/twisters/')
async def add_twister(twister: schemas.Twister) -> schemas.Twister:
    if await service.check_twister_similarity(twister):
        raise HTTPException(status_code=400, detail='similar twister already exists')
    return await service.add_twister(twister)


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
