import os 
if not os.path.exists("logs"):
    os.makedirs("logs", exist_ok=True)

port = os.environ["FASTAPI_PORT"] if "FASTAPI_PORT" in os.environ else 8000
bind = f"0.0.0.0:{port}"
accesslog = "logs/access.log"
errorlog = "logs/error.log"
workers = 1
threads = 2
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 1800
graceful_timeout = 300
keepalive = 15
proc_name = "API"