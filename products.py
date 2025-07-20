from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse
from app.dependencies import get_current_user
from app.models import user as user_model
from app.models import product as product_model

router = APIRouter(prefix="/products", tags=["products"])

# Get all products
@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# Create a product
@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user: user_model.User = Depends(get_current_user)):
    db_product = product_model.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Get one product
@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Update product
@router.put("/{product_id}")
def update_product(product_id: int, product_data: dict, db: Session = Depends(get_db)):
    product = db.query(Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product_data.items():
        setattr(product, key, value)
    db.commit()
    return product

# Delete product
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted"}
