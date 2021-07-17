from enum import unique
from typing_extensions import TypeGuard
from tortoise.models import Model
from tortoise import fields

__all__ = ["User"]


class User(Model):
    # primary key assigned to each user in database
    _id = fields.IntField(pk=True)
    # telegram user id wich is unique to each user, gathered from telegram api
    telegram_user_id = fields.IntField(unique=True)
    # username gathered from telegram api
    name = fields.TextField()
    # table for all user submites to all challenges
    submits = fields.ManyToManyField('models.ChallengeSubmit')

    def __str__(self):
        return "[user -> {}, with id -> {}]".format(self.name, self.telegram_user_id)
