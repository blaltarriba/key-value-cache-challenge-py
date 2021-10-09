from cache.models.item import Item
from cache.repositories.item_repository import ItemRepository
from cache.repositories.item_cached_repository import ItemCachedRepository

class Cache():
    def __init__(self, item_repository: ItemRepository, item_cached_repository: ItemCachedRepository):
        self.item_repository = item_repository
        self.item_cached_repository = item_cached_repository

    def fetch(self, code: str) -> Item:
        item = self.item_repository.getById(code)
        return item