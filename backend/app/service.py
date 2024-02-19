from difflib import get_close_matches

from backend.app import schemas, models


async def add_twister(data: schemas.Twister) -> models.Twister:
    return await models.Twister.create(**data.dict(exclude={'id'}))


async def get_all_twisters() -> list[models.Twister]:
    return await models.Twister.all()


async def check_twister_similarity(data: schemas.Twister) -> bool:
    existing_twisters = await models.Twister.all().values_list('text', flat=True)
    return bool(get_close_matches(data.text, existing_twisters))
