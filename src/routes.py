from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from cache.services.cache import Cache
from cache.models.item import Item
from cache.repositories.item_repository import ItemRepository
from cache.repositories.item_cached_repository import ItemCachedRepository

router = APIRouter()
item_repository = ItemRepository(items = { 'a_code': Item(code='a_code', description='a_description') })
item_cached_repository = ItemCachedRepository()
cache = Cache(item_repository=item_repository, item_cached_repository=item_cached_repository)


@router.get("/fetch/{item_code}")
def fetch_item(item_code: str) -> Item:
    item = cache.fetch(item_code)

    if not item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No item found with that id.")

    return item
