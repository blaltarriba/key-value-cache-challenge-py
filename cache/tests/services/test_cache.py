import pytest
from cache.models.item import Item
from cache.services.cache import Cache
from cache.repositories.item_repository import ItemRepository

class TestCache:

    def test_fecth_item_return_item_when_exists(self) -> None:
        item = Item(code='a_code', description='a_description')
        item_repository = ItemRepository(items={ item.code: item })
        cache = Cache(item_repository=item_repository)

        result = cache.fetch(item.code)

        assert result.code == item.code
        assert result.description == item.description

    def test_fecth_item_return_none_when_does_not_exists(self) -> None:
        item_repository = ItemRepository(items={})
        cache = Cache(item_repository=item_repository)

        result = cache.fetch('fake')

        assert result is None