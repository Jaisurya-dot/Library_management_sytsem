from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from routers.auth import router as auth_router
from db.database import create_tables
import models.story
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app=FastAPI(
    title="Library Management",
    description="A handy managemnet sysytem",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"], #"GET","POST","PUT","DELETE"
    allow_headers=["*"],
)


app.include_router(auth_router, prefix=settings.API_PREFIX)


if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0",port=8000,reload=True)
