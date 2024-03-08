from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from func import *

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
load_route(app)

Instrumentator().instrument(app).expose(app)