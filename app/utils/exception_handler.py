from fastapi.requests import Request
from fastapi.responses import JSONResponse


class InvalidLanguageError(Exception):
    def __init__(self, error_input_key: str, error_input_value: str):
        self.code = 400
        self.name = "InvalidLanguageError"
        self.message = f"The input {error_input_key} `{error_input_value}` is an invalid language, please check."


async def general_error_handler(request: Request, exc):
    return JSONResponse(status_code=exc.code, content={"error": {"name": exc.name, "message": exc.message}})


def load_exception_handler(app):
    exception_list = [InvalidLanguageError]
    for exc in exception_list:
        app.exception_handler(exc)(general_error_handler)
