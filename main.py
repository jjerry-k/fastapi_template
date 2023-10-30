from fastapi import FastAPI, APIRouter
from func import *
from routes import route1, route2

app = FastAPI()

router = APIRouter(
    prefix="",
    tags=["Basic"]
)

@router.get('/')
async def root():
    return 

@router.get('/health')
async def health():
    return {'success': True}

app.include_router(router)
app.include_router(route1.router)
app.include_router(route2.router)