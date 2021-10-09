from typing import Optional
from cache.models.item import Item


class ItemCachedRepository():
    def __init__(self, items: Optional[dict[str, Item]] = {}):
        self.items = items

    def getById(self, code: str) -> Item:
        return self.items.get(code)

    def persist(self, item: Item) -> None:
        self.items[item.code] = item
