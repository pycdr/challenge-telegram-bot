from tortoise import Tortoise
from anna.models.challenge import Challenge, ChallengeSubmit
from anna.models.user import User

__all__ = ["User", "Challenge", "ChallengeSubmit", "init"]


async def init():
    # Here we connect to a SQLite DB file.
    # also specify the app name of "models"
    # which contain models from "app.models"
    await Tortoise.init(
        db_url='sqlite://db.sqlite',
        modules={'models': ['anna.models.user', 'anna.models.challenge']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
