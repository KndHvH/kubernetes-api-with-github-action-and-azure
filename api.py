

from fastapi import FastAPI
from routers import health_check
from routers import root

app = FastAPI()

app.include_router(health_check.router)
app.include_router(root.router)