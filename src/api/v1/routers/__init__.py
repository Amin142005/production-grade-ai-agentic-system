"""API v1 routers package."""



from .base import router as base_router
from .auth import router as auth_router

__all__ = ["base_router", "auth_router"]