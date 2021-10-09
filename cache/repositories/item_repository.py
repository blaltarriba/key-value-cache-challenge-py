from cache.models.item import Item


class ItemRepository():
    items: dict[str, Item] = { 'a_code': Item(code='a_code', description='a_description') }

    def getById(self, code: str) -> Item:
        return self.items.get(code)
