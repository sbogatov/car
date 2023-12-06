from fastapi import FastAPI

from brand.controllers import brand_router
from car_model.controllers import car_model_router

app = FastAPI()

app.include_router(brand_router)
app.include_router(car_model_router)