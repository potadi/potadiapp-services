from fastapi import FastAPI
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000)