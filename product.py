from pydantic import BaseModel

# Request schema for creating a product
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int

# Response schema for returning a product
class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True
