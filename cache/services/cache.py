from cache.models.item import Item


class Cache():
    items: dict[str, Item] = {}

    def fetch(self, code: str) -> Item:
        item = self.items.get(code)
        if item:
            return item
        return Item(code=code, description='a_description')