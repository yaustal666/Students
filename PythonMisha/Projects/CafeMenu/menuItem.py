from pydantic import BaseModel

class MenuItem(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    category: str
