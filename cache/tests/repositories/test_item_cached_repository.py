import pytest

from cache.models.item import Item
from cache.repositories.item_cached_repository import ItemCachedRepository

class TestItemCachedRepository:

    @pytest.fixture
    def an_item(self) -> Item:
        return Item(code='a_code', description='a_description')

    def test_getById_return_item_when_exists(self, an_item: Item, an_item_cached_repository_with_item: ItemCachedRepository) -> None:
        result = an_item_cached_repository_with_item.getById(an_item.code)

        assert result.code == an_item.code
        assert result.description == an_item.description

    def test_getById_item_return_none_when_does_not_exists(self, an_item_cached_repository_with_item: ItemCachedRepository) -> None:
        result = an_item_cached_repository_with_item.getById('fake')

        assert result is None

    def test_persist_item_when_did_not_exists_before(self, an_item: Item) -> None:
        item_cached_repository = ItemCachedRepository(items={})

        item_cached_repository.persist(an_item)

        assert len(item_cached_repository.items) == 1
