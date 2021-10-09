import uvicorn
# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel, Field
#
# app = FastAPI()
#
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
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/users/{user_id}")
# def read_user(user_id: int):
#     return {"user_id": user_id, "full_name": "Danny Manny", "email": "danny.manny@gmail.com"}
#
#
# @app.post("/users/add")
# def add_user(user: User):
#     return {"full_name": user.first_name+" "+user.last_name}
#
#
# @app.put("/users/update")
# def update_user(user: User):
#     return {"user_id": user.user_id, "full_name": user.first_name+" "+user.last_name, "email": user.email}
#
#
# @app.delete("/users/{user_id}/delete")
# def delete_user(user_id: int):
#     return {"user_id": user_id, "is_deleted": True}

from server import app


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8005)
    print("running")