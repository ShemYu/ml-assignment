from fastapi import FastAPI

from app.endpoints.translation import router as translation_router
from app.utils.load_model import load_model


app = FastAPI()
app.include_router(translation_router)


@app.on_event("startup")
async def startup_event():
    _, _ = await load_model()


@app.get("/healthz")
async def health_check():
    return {"status": "OK"}
