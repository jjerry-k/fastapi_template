from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import make_asgi_app

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

metrics_app = make_metrics_app()
app.mount("/metrics", metrics_app)