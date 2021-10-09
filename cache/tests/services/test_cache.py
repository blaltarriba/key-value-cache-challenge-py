import pytest
from pytest_mock import MockerFixture
from cache.models.item import Item
from cache.services.cache import Cache
from cache.repositories.item_repository import ItemRepository
from cache.repositories.item_cached_repository import ItemCachedRepository

class TestCache:

    @pytest.fixture
    def an_item_repository(self, an_item) -> ItemRepository:
        return ItemRepository(items={ an_item.code: an_item })

    @pytest.fixture
    def an_item_cached_repository(self, an_item) -> ItemCachedRepository:
        return ItemCachedRepository(items={})

    @pytest.fixture
    def a_cache_service(self, an_item_repository, an_item_cached_repository) -> Cache:
        return Cache(item_repository=an_item_repository, item_cached_repository=an_item_cached_repository)

    def test_fetch_item_return_item_when_exists(self, a_cache_service: Cache, an_item: Item) -> None:

        result = a_cache_service.fetch(an_item.code)

        assert result.code == an_item.code
        assert result.description == an_item.description

    def test_fetch_item_return_none_when_does_not_exists(self, a_cache_service: Cache) -> None:

        result = a_cache_service.fetch('fake')

        assert result is None

    def test_fetch_item_store_in_cache_when_did_not_exists(self, an_item: Item, a_cache_service: Cache, an_item_cached_repository: ItemCachedRepository, mocker: MockerFixture) -> None:
        item_cached_repository_spy = mocker.spy(ItemCachedRepository, 'persist')

        result = a_cache_service.fetch(an_item.code)

        item_cached_repository_spy.assert_called_once()
        assert result.code == an_item.code

    def test_fetch_item_retrieve_from_cache_when_exists(self, an_item: Item, an_item_repository: ItemRepository, an_item_cached_repository_with_item: ItemCachedRepository,mocker: MockerFixture) -> None:
        cache_service = Cache(item_repository=an_item_repository, item_cached_repository=an_item_cached_repository_with_item)
        item_repository_spy = mocker.spy(ItemRepository, 'getById')

        result = cache_service.fetch(an_item.code)

        item_repository_spy.assert_not_called()
        assert result.code == an_item.code
