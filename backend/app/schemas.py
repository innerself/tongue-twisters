from pydantic import BaseModel


class Twister(BaseModel):
    id: int | None = None
    text: str
    language: str
