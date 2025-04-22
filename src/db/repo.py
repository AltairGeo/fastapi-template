from abc import abstractmethod, ABC
from typing import List, Dict, Any

class AbstractRepo[T](ABC):
    @abstractmethod
    async def add(self, data: Dict[Any]) -> T:
        raise NotImplementedError

    @abstractmethod
    async def add_many(self, data: List[dict]) -> List[T]:
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, **filters) -> T:
        raise NotImplementedError
    
    @abstractmethod
    async def get_all(self, **filters) -> List[T]:
        raise NotImplementedError

    @abstractmethod
    async def get_all_with_paginate(self, page: int, **filters) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def update(self, data: dict, **filters) -> T:
        raise NotImplementedError

    @abstractmethod
    async def remove(self, **filters) -> bool:
        raise NotImplementedError