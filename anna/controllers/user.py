from anna.controllers.base import CRUD
from anna.models import User, ChallengeSubmit, user

__all__ = ["UserManager"]


class UserManager(CRUD):
    """Manager stack for user database
    """

    async def create(self, userid: int, username: str):
        await User.create(
            telegram_user_id=userid, name=username)

    async def update(self, pk: int, challenge_submit: ChallengeSubmit):
        """Update user data i.e. rename username
        """
        user = await User.filter(_id=pk)
        await user.submits.add([challenge_submit])

    async def delete(self, pk: int):
        await User.filter(_id=pk).delete()

    async def search(self, userid: str) -> User:
        """Search user by telegram user id
        """
        return await User.filter(
            telegram_user_id=userid)
