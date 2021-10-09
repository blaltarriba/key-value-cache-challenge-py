import pytest
from cache.models.item import Item
from cache.services.cache import Cache
from cache.repositories.item_repository import ItemRepository
from cache.repositories.item_cached_repository import ItemCachedRepository

class TestCache:

    @pytest.fixture
    def an_item(self):
        return Item(code='a_code', description='a_description')

    @pytest.fixture
    def an_item_repository(self, an_item):
        return ItemRepository(items={ an_item.code: an_item })

    @pytest.fixture
    def an_item_cached_repository(self, an_item):
        return ItemCachedRepository(items={})

    @pytest.fixture
    def a_cache_service(self, an_item_repository, an_item_cached_repository):
        return Cache(item_repository=an_item_repository, item_cached_repository=an_item_cached_repository)

    def test_fecth_item_return_item_when_exists(self, a_cache_service: Cache, an_item: Item) -> None:

        result = a_cache_service.fetch(an_item.code)

        assert result.code == an_item.code
        assert result.description == an_item.description

    def test_fecth_item_return_none_when_does_not_exists(self, a_cache_service: Cache) -> None:

        result = a_cache_service.fetch('fake')

        assert result is None

    