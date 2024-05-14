__all__ = [
    "start_app",
    "init_routers"
]

from .routers import init_routers
from .web import start_app
