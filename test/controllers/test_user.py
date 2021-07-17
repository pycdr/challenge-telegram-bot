import pytest
from anna.controllers.user import UserManager
from anna.models import init
import random

manager = UserManager()


@pytest.mark.asyncio
async def test_user_create():
    random_userid = random.randint(5, 500)
    await init()
    _ = await manager.create(
        userid=random_userid, username="rickandmorty")


@pytest.mark.asyncio
async def test_searching_user():
    await init()
    result = await manager.search(userid=123124123)
    print(result)
    if len(result) < 1:
        AssertionError("manager didn't find user which was created.")


@pytest.mark.asyncio
async def test_delete_user():
    await init()
    user = await manager.search(userid=123124123)
    await manager.delete(pk=user[0]._id)
