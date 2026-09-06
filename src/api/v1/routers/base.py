"""Base router with core utility endpoints."""

from datetime import UTC, datetime

from fastapi import APIRouter

from config.settings import setting
from system.logs import logger

router = APIRouter()


@router.get("/health")
async def health_check():
    """Return application health status.

    Returns:
        dict: App name, version, current UTC datetime, and status string.
    """
    logger.info("health_check_called")
    return {
        "app_name": setting.PROJECT_NAME,
        "version": setting.VERSION,
        "current_datetime": datetime.now(UTC),
        "status": "healthy",
    }