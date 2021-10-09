from cache.models.item import Item
from cache.repositories.item_repository import ItemRepository


class Cache():
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def fetch(self, code: str) -> Item:
        item = self.item_repository.getById(code)
        return item