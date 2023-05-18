from fastapi import FastAPI
from routes.app_routes import home

app = FastAPI(
    title="Data validation",
    description="An example of data validation in FastAPI",
    version="1.0",
)

app.include_router(home)
