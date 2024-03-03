from pydantic import BaseModel

from backend.app.models import TwisterLanguage


class Twister(BaseModel):
    id: int | None = None
    text: str
    language: TwisterLanguage
