from fastapi import FastAPI

from app.endpoints.translation import router as translation_router
from app.utils import exception_handler, load_model


app = FastAPI(
    title="Translation Service API",
    description="This is a translation service API that translates text between different languages.",
    version="1.0.0",
)
app.include_router(translation_router)
exception_handler.load_exception_handler(app)


@app.on_event("startup")
async def startup_event():
    """Startup event to load the translation model.

    This function loads the translation model when the application starts.

    Returns:
        None
    """
    _ = await load_model.load_model()


@app.get("/healthz")
async def health_check():
    """Health check endpoint.

    This endpoint is used to check the health of the application.
    A successful response indicates that the application is running as expected.

    Returns:
        dict: A JSON object with a single key `status` with a value of "OK".
    """
    return {"status": "OK"}
