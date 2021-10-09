import pytest
from cache.models.item import Item
from cache.repositories.item_cached_repository import ItemCachedRepository

@pytest.fixture
def an_item() -> Item:
    return Item(code='a_code', description='a_description')

@pytest.fixture
def an_item_cached_repository_with_item(an_item: Item) -> ItemCachedRepository:
    return ItemCachedRepository(items={an_item.code: an_item})