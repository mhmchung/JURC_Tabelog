from fastapi import FastAPI
from routers import customers, restaurants, dishes
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="餐廳評論系統 API",
    description="一個用於管理客戶、餐廳、菜色和評論的 RESTful API。",
    version="1.0.0"
)

# Include API routers
app.include_router(customers.router)
app.include_router(restaurants.router)
app.include_router(dishes.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Restaurant Review API!"}
