from fastapi import FastAPI

from app.endpoints.translation import router as translation_router
from app.utils import exception_handler, load_model


app = FastAPI()
app.include_router(translation_router)


@app.on_event("startup")
async def startup_event():
    exception_handler.load_exception_handler(app)
    _ = await load_model.load_model()


@app.get("/healthz")
async def health_check():
    return {"status": "OK"}
