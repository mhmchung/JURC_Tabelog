from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List, Dict, Any
from decimal import Decimal

# --- Customer Schemas ---
class CustomerBase(BaseModel):
    nick_name: Optional[str] = None
    phone: Optional[str] = None
    avatar_url: Optional[str] = None
    basic_info: Optional[str] = None
    preference_type: Optional[str] = None
    last_active_at: Optional[datetime] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    churn_rate: float
    review_count: int
    created_at: datetime

    class Config:
        orm_mode = True

# --- AuthAccount Schemas ---
class AuthAccountCreate(BaseModel):
    provider: str
    provider_id: Optional[str] = None
    email: Optional[EmailStr] = None
    password_hash: Optional[str] = None

# --- Restaurant Schemas ---
class RestaurantBase(BaseModel):
    google_place_id: Optional[str] = None
    name: str
    phone_number: Optional[str] = None
    location: Optional[str] = None
    accessibility: Optional[str] = None
    parking: Optional[bool] = False
    type: Optional[str] = None
    price_range: Optional[str] = None
    vibe: Optional[str] = None
    average_waiting_time: Optional[int] = None
    online_reservation: Optional[bool] = False
    opening_hours: Optional[str] = None
    website_url: Optional[str] = None
    menu_url: Optional[str] = None
    hours_of_operation: Optional[Dict[str, Any]] = None

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantResponse(RestaurantBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# --- Dish Schemas ---
class DishBase(BaseModel):
    restaurant_id: int
    name: str
    type: Optional[str] = None
    price: Optional[Decimal] = None
    taste: Optional[str] = None
    portion: Optional[str] = None
    info: Optional[str] = None
    is_pr: Optional[bool] = False

class DishCreate(DishBase):
    pass

class DishResponse(DishBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# --- RestaurantReview Schemas ---
class RestaurantReviewBase(BaseModel):
    customer_id: Optional[int] = None
    restaurant_id: int
    tasty_score: Optional[int] = None
    service_score: Optional[int] = None
    ambience_score: Optional[int] = None
    comment: Optional[str] = None
    visit_time: Optional[datetime] = None
    is_anonymous: Optional[bool] = False

class RestaurantReviewCreate(RestaurantReviewBase):
    pass

class RestaurantReviewResponse(RestaurantReviewBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# --- DishReview Schemas ---
class DishReviewBase(BaseModel):
    customer_id: Optional[int] = None
    restaurant_id: int
    dish_id: int
    score: Optional[int] = None
    comment: Optional[str] = None
    is_anonymous: Optional[bool] = False

class DishReviewCreate(DishReviewBase):
    pass

class DishReviewResponse(DishReviewBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# --- Combined Response Schemas ---
class DishWithReviewsResponse(DishResponse):
    dish_reviews: List[DishReviewResponse] = []

class RestaurantWithDetailsResponse(RestaurantResponse):
    dishes: List[DishWithReviewsResponse] = []
    restaurant_reviews: List[RestaurantReviewResponse] = []
