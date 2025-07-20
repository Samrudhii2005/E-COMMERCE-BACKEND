from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import order as order_model, product as product_model
from app.schemas.order import OrderCreate, OrderOut
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrderOut)
def place_order(
    order_data: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(product_model.Product).filter(product_model.Product.id == order_data.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.stock < order_data.quantity:
        # Create order with failed status
        order = order_model.Order(
            user_id=current_user.id,
            product_id=order_data.product_id,
            quantity=order_data.quantity,
            status="failed"
        )
        db.add(order)
        db.commit()
        db.refresh(order)
        return order

    # Subtract stock
    product.stock -= order_data.quantity
    db.commit()

    # Create confirmed order
    order = order_model.Order(
        user_id=current_user.id,
        product_id=order_data.product_id,
        quantity=order_data.quantity,
        status="confirmed"
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@router.get("/", response_model=list[OrderOut])
def get_my_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    orders = db.query(order_model.Order).filter(order_model.Order.user_id == current_user.id).all()
    return orders

@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    order = db.query(order_model.Order).filter(
        order_model.Order.id == order_id,
        order_model.Order.user_id == current_user.id
    ).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    db.delete(order)
    db.commit()
    return {"message": "Order cancelled successfully"}
