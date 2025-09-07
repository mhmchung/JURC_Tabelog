from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Dish, DishReview, Restaurant
from schemas import DishCreate, DishResponse, DishReviewCreate, DishReviewResponse

router = APIRouter(
    prefix="/dishes",
    tags=["Dishes"]
)

@router.post("/", response_model=DishResponse, status_code=status.HTTP_201_CREATED)
def create_dish(dish: DishCreate, db: Session = Depends(get_db)):
    """
    Create a new dish for a specific restaurant.
    """
    restaurant = db.query(Restaurant).filter(Restaurant.id == dish.restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
    
    new_dish = Dish(**dish.dict())
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return new_dish

@router.post("/{dish_id}/reviews", response_model=DishReviewResponse, status_code=status.HTTP_201_CREATED)
def create_dish_review(dish_id: int, review: DishReviewCreate, db: Session = Depends(get_db)):
    """
    Add a new review to a dish.
    """
    dish = db.query(Dish).filter(Dish.id == dish_id).first()
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dish not found")
    
    new_review = DishReview(dish_id=dish_id, **review.dict(exclude={"dish_id"}))
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review
