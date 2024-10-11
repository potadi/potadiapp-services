from fastapi import FastAPI
import hypercorn.asyncio
from middleware.cors import add_cors_middleware
from diagnoses.router import router

app = FastAPI(
    title="API Service for potadi.ai",
    description="API Service for potadi.ai",
    version="1.0.0"
)

# Prefix for diagnoses router
app.include_router(router, tags=['diagnose'])

add_cors_middleware(app)
