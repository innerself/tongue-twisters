import random
from difflib import get_close_matches

from backend.app import schemas, models
from backend.app.models import TwisterLanguage


async def add_twister(data: schemas.Twister) -> models.Twister:
    return await models.Twister.create(**data.dict(exclude={'id'}))


async def get_all_twisters(number: int, language: TwisterLanguage | None) -> list[models.Twister]:
    all_ids = await models.Twister.all().values_list('id', flat=True)
    flt = {'id__in': random.sample(all_ids, k=number)}
    if language:
        flt['language'] = language

    return await models.Twister.filter(**flt)


async def check_twister_similarity(data: schemas.Twister) -> bool:
    existing_twisters = await models.Twister.all().values_list('text', flat=True)
    return bool(get_close_matches(data.text, existing_twisters))
