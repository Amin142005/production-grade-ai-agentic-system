"""FastAPI application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse

from api.v1 import v1_router
from config.settings import setting
from data.db_manager import db_manager
from system.logs import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application startup and shutdown lifecycle."""

    logger.info(
        "application_startup",
        project_name=setting.PROJECT_NAME,
        version=setting.VERSION,
        api_version=setting.API_VERSION,
    )

    # await db_manager.check_connection()
    logger.info("database_connection_successful")

    try:
        yield
    finally:
        logger.info("application_shutdown")

    
    
    
app = FastAPI(
    title=setting.PROJECT_NAME,
    version=setting.VERSION,
    openapi_url=f"{setting.API_VERSION}/openapi.json",
    lifespan=lifespan,
)

app.include_router(v1_router)