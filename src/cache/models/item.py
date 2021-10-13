from pydantic import BaseModel

class Item(BaseModel):
    code: str
    description: str