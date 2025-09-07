from sqlalchemy import Column, Integer, String, Text, Boolean, REAL, DateTime, ForeignKey, Numeric, JSON
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from database import Base

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    nick_name = Column(String(50))
    phone = Column(String(20))
    avatar_url = Column(Text)
    basic_info = Column(Text)
    preference_type = Column(String(50))
    churn_rate = Column(REAL, default=0.0)
    review_count = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())
    last_active_at = Column(DateTime)

    auth_accounts = relationship("AuthAccount", back_populates="customer", cascade="all, delete-orphan")
    restaurant_reviews = relationship("RestaurantReview", back_populates="customer", cascade="all, delete-orphan")
    dish_reviews = relationship("DishReview", back_populates="customer", cascade="all, delete-orphan")

class AuthAccount(Base):
    __tablename__ = 'auth_accounts'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id', ondelete='CASCADE'), nullable=False)
    provider = Column(String(50), nullable=False)
    provider_id = Column(String(100))
    email = Column(String(100))
    password_hash = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

    customer = relationship("Customer", back_populates="auth_accounts")

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    google_place_id = Column(String(255), unique=True)
    name = Column(String(100), nullable=False)
    phone_number = Column(String(20))
    location = Column(Text)
    accessibility = Column(Text)
    parking = Column(Boolean, default=False)
    type = Column(String(50))
    price_range = Column(String(50))
    vibe = Column(Text)
    average_waiting_time = Column(Integer)
    online_reservation = Column(Boolean, default=False)
    opening_hours = Column(Text)
    website_url = Column(Text)
    menu_url = Column(Text)
    hours_of_operation = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())

    dishes = relationship("Dish", back_populates="restaurant", cascade="all, delete-orphan")
    restaurant_reviews = relationship("RestaurantReview", back_populates="restaurant", cascade="all, delete-orphan")

class Dish(Base):
    __tablename__ = 'dishes'
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(100), nullable=False)
    type = Column(String(50))
    price = Column(Numeric(10, 2))
    taste = Column(Text)
    portion = Column(Text)
    info = Column(Text)
    is_pr = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    restaurant = relationship("Restaurant", back_populates="dishes")
    dish_reviews = relationship("DishReview", back_populates="dish", cascade="all, delete-orphan")

class RestaurantReview(Base):
    __tablename__ = 'restaurant_reviews'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id', ondelete='SET NULL'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id', ondelete='CASCADE'), nullable=False)
    tasty_score = Column(Integer)
    service_score = Column(Integer)
    ambience_score = Column(Integer)
    comment = Column(Text)
    visit_time = Column(DateTime)
    is_anonymous = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    customer = relationship("Customer", back_populates="restaurant_reviews")
    restaurant = relationship("Restaurant", back_populates="restaurant_reviews")

class DishReview(Base):
    __tablename__ = 'dish_reviews'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id', ondelete='SET NULL'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id', ondelete='CASCADE'), nullable=False)
    dish_id = Column(Integer, ForeignKey('dishes.id', ondelete='CASCADE'), nullable=False)
    score = Column(Integer)
    comment = Column(Text)
    is_anonymous = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    customer = relationship("Customer", back_populates="dish_reviews")
    dish = relationship("Dish", back_populates="dish_reviews")
