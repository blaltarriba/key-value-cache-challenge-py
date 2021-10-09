from typing import Optional
from cache.models.item import Item


class ItemRepository():
    def __init__(self, items: Optional[dict[str, Item]] = { 'a_code': Item(code='a_code', description='a_description') }):
        self.items = items

    def getById(self, code: str) -> Item:
        return self.items.get(code)
