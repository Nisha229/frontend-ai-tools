from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router  # import your routes

app = FastAPI(
    title="AI Text Processing API",
    description="API for text processing using various AI models with strategy pattern",
    version="1.0.0",
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)
