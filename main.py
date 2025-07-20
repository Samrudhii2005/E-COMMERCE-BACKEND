from fastapi import FastAPI
from app.routers import auth, products, orders
from app.database import Base, engine
from app.models import product

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    description="Backend API for managing users, products, carts, and orders.",
    version="1.0.0",
    contact={
        "name": "Samrudhi Ghanate",
        "email": "sam@gmail.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)