from fastapi.requests import Request
from fastapi.responses import JSONResponse


class InvalidLanguageError(Exception):
    """
    Custom exception raised for invalid language inputs.

    Attributes:
        code (int): The HTTP status code for the error, typically 400.
        name (str): The name of the error, "InvalidLanguageError."
        message (str): A user-friendly error message.
    """

    def __init__(self, error_input_key: str, error_input_value: str):
        self.code = 400
        self.name = "InvalidLanguageError"
        self.message = f"The input {error_input_key} `{error_input_value}` is an invalid language, please check."


async def general_error_handler(request: Request, exc):
    """
    General error handler function.

    Args:
        request (Request): The request object.
        exc (Exception): The exception raised.

    Returns:
        JSONResponse: A JSON response containing the error details.
    """
    return JSONResponse(status_code=exc.code, content={"error": {"name": exc.name, "message": exc.message}})


def load_exception_handler(app):
    """
    Function to load custom exception handlers into the FastAPI app.

    Args:
        app: The FastAPI app instance.
    """
    exception_list = [InvalidLanguageError]
    for exc in exception_list:
        app.exception_handler(exc)(general_error_handler)
