from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from backend.models import Restaurant, RestaurantReview
from schemas import RestaurantCreate, RestaurantResponse, RestaurantReviewCreate, RestaurantReviewResponse, RestaurantWithDetailsResponse

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"]
)

@router.post("/", response_model=RestaurantResponse, status_code=status.HTTP_201_CREATED)
def create_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    """
    Create a new restaurant.
    """
    new_restaurant = Restaurant(**restaurant.dict())
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    return new_restaurant

@router.get("/", response_model=List[RestaurantResponse])
def get_all_restaurants(db: Session = Depends(get_db)):
    """
    Get a list of all restaurants.
    """
    return db.query(Restaurant).all()

@router.get("/{restaurant_id}", response_model=RestaurantWithDetailsResponse)
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    """
    Get a single restaurant with its dishes and reviews.
    """
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
    
    return restaurant

@router.post("/{restaurant_id}/reviews", response_model=RestaurantReviewResponse, status_code=status.HTTP_201_CREATED)
def create_restaurant_review(restaurant_id: int, review: RestaurantReviewCreate, db: Session = Depends(get_db)):
    """
    Add a new review to a restaurant.
    """
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
    
    new_review = RestaurantReview(restaurant_id=restaurant_id, **review.dict(exclude={"restaurant_id"}))
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review
