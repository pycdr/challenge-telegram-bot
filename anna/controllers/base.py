from abc import ABC, abstractclassmethod

class CRUD(ABC):
    """Inherite this class to create database manager stack.
    """

    @abstractclassmethod
    async def create(self, *args, **kwargs):
        raise NotImplemented("create method not implemented")

    @abstractclassmethod
    async def update(self, *args, **kwargs):
        raise NotImplemented("update method not implemented")

    @abstractclassmethod
    async def delete(self, *args, **kwargs):
        raise NotImplemented("delete method not implemented")

    @abstractclassmethod
    async def search(self, *args, **kwargs):
        raise NotImplemented("search method not implemented")