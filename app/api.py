

from fastapi import FastAPI
from app.routers import health_check
from app.routers import root

app = FastAPI()

app.include_router(health_check.router)
app.include_router(root.router)