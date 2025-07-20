from app.database import engine, Base
from app.models.product import Product
from app.models.user import User

# Create all tables
Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")
