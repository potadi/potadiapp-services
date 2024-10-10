from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    origins = [
        'http://localhost:8000',
        ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*", "X-Requested-With", "Content-Type"],
        # expose_headers=["Content-Disposition"],
    )