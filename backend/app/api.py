from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

from . import schemas, service
from .models import TwisterLanguage

router = APIRouter()


@router.get('/twisters/')
async def get_twisters_list(number: Annotated[int, Query(gt=0)] = 3,
                            language: TwisterLanguage | None = None) -> list[schemas.Twister]:
    return await service.get_all_twisters(number=number, language=language)


@router.post('/twisters/')
async def add_twister(twister: schemas.Twister) -> schemas.Twister:
    if await service.check_twister_similarity(twister):
        raise HTTPException(status_code=400, detail='similar twister already exists')
    return await service.add_twister(twister)


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
