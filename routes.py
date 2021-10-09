# from typing import List
#
# from fastapi import APIRouter, Body, Depends, HTTPException
#
# from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
#
# from app.models.cleaning import CleaningCreate, CleaningPublic
# from app.db.repositories.cleanings import CleaningsRepository
# from app.api.dependencies.database import get_repository
#
#
# router = APIRouter()
#
#
# @router.get("/")
# async def get_all_cleanings() -> List[dict]:
#     cleanings = [
#         {"id": 1, "name": "My house", "cleaning_type": "full_clean", "price_per_hour": 29.99},
#         {"id": 2, "name": "Someone else's house", "cleaning_type": "spot_clean", "price_per_hour": 19.99},
#     ]
#
#     return cleanings
#
#
# @router.get("/{id}/", response_model=CleaningPublic, name="cleanings:get-cleaning-by-id")
# async def get_cleaning_by_id(
#     id: int, cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository))
# ) -> CleaningPublic:
#     cleaning = await cleanings_repo.get_cleaning_by_id(id=id)
#
#     if not cleaning:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No cleaning found with that id.")
#
#     return cleaning
#
#
# @router.post("/", response_model=CleaningPublic, name="cleanings:create-cleaning", status_code=HTTP_201_CREATED)
# async def create_new_cleaning(
#     new_cleaning: CleaningCreate = Body(..., embed=True),
#     cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
# ) -> CleaningPublic:
#     created_cleaning = await cleanings_repo.create_cleaning(new_cleaning=new_cleaning)
#
#     return created_cleaning



# from typing import Optional
from fastapi import APIRouter
# from pydantic import BaseModel, Field
from cache.services.cache import Cache
from cache.models.item import Item

router = APIRouter()
cache = Cache()

# class User(BaseModel):
#     user_id: Optional[int] = None
#     first_name: str
#     last_name: str
#     email: str
#     father_name: Optional[str] = Field(
#         None, title="The father name of the user", max_length=300
#     )
#     age: float = Field(..., gt=0,
#                        description="The age must be greater than zero")


@router.get("/fetch/{item_code}")
def fetch_item(item_code: str) -> Item:
    return cache.fetch(item_code)

@router.get("/")
def read_root():
    return {"Hello": "World"}


# @router.get("/users/{user_id}")
# def read_user(user_id: int):
#     return {"user_id": user_id, "full_name": "Danny Manny", "email": "danny.manny@gmail.com"}
#
#
# @router.post("/users/add")
# def add_user(user: User):
#     return {"full_name": user.first_name+" "+user.last_name}
#
#
# @router.put("/users/update")
# def update_user(user: User):
#     return {"user_id": user.user_id, "full_name": user.first_name+" "+user.last_name, "email": user.email}
#
#
# @router.delete("/users/{user_id}/delete")
# def delete_user(user_id: int):
#     return {"user_id": user_id, "is_deleted": True}
