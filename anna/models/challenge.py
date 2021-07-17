from tortoise.models import Model
from tortoise import fields

__all__ = ["Challenge", "ChallengeSubmit"]


class Challenge(Model):
    # primary key assigned to each challenge in database
    _id = fields.IntField(pk=True)
    # short description title
    title = fields.TextField()
    # challenge content in form of text
    content = fields.TextField()

    def __str__(self):
        return "[challenge with title -> {}]".format(self.title)


class ChallengeSubmit(Model):
    # primary key assigner to each challenge in database
    _id = fields.IntField(pk=True)
    # user who submitted answer to challenge
    submitter = fields.ForeignKeyField('models.User')
    # challenge which user submitted solution to.
    challenge = fields.ForeignKeyField('models.Challenge')
    # solution which user submmited to challenge in form of text
    solution = fields.TextField()

    def __str__(self):
        return "[solution from userid -> {} for challenge id -> {}]".format(self.submit, self.challenge)
