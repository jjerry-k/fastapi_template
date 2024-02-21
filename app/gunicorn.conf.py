import os 
if not os.path.exists("logs"):
    os.makedirs("logs", exist_ok=True)
    
bind = f"0.0.0.0:{os.environ['PORT']}"
accesslog = "logs/access.log"
errorlog = "logs/error.log"
workers = 1
threads = 2
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 1800
graceful_timeout = 300
keepalive = 15
proc_name = "API"