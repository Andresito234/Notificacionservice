from fastapi import FastAPI
from app.presentation.api import router as api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)