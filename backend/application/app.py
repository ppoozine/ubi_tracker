from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .urls.api_urls import init_apis
from .database import database
from .log.log import logger

def create_app():
    app = FastAPI(
        title="Ubi API using FastAPI PostgreSQL Async EndPoints",
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        version="0.1.0",
        description="This is the API docs that provides UBI dashboard.",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    init_apis(app)

    @app.on_event("startup")
    @logger.catch
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    @logger.catch
    async def shutdown():
        await database.disconnect()

    @app.get('/host')
    async def index():
        return {"status": "host on"}
    
    return app