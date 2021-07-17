import pytest
from anna.models import init


@pytest.mark.asyncio
async def test_init_database():
    # intialize sqlite database
    await init()
