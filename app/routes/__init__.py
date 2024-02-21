import os
dir_path = os.path.dirname(__file__)
route_list = os.listdir(dir_path)

for route in route_list:
    if os.path.isdir(os.path.join(dir_path, route)) and route != "__pycache__":
        exec(f"from .{route} import *")