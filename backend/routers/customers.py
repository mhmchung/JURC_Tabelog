from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from backend.models import Customer, AuthAccount
from schemas import CustomerCreate, CustomerResponse, AuthAccountCreate

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post("/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """
    Create a new customer.
    """
    new_customer = Customer(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Get customer details by ID.
    """
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, customer_data: CustomerCreate, db: Session = Depends(get_db)):
    """
    Update customer information.
    """
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    
    for key, value in customer_data.dict(exclude_unset=True).items():
        setattr(customer, key, value)
    
    db.commit()
    db.refresh(customer)
    return customer
