import enum

from tortoise import models, fields


class TwisterLanguage(enum.StrEnum):
    EN = 'en'
    RU = 'ru'


class Twister(models.Model):
    id = fields.IntField(pk=True)
    text = fields.TextField()
    language = fields.CharEnumField(TwisterLanguage)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
