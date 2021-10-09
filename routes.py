from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from cache.services.cache import Cache
from cache.models.item import Item
from cache.repositories.item_repository import ItemRepository

router = APIRouter()
item_repository = ItemRepository()
cache = Cache(item_repository=item_repository)


@router.get("/fetch/{item_code}")
def fetch_item(item_code: str) -> Item:
    item = cache.fetch(item_code)

    if not item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No item found with that id.")

    return item
