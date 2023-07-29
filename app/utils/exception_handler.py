from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse


class InvalidLanguageError(Exception):
    def __init__(self, error_input_key: str, error_input_value: str):
        self.code = 400
        self.message = f"The input {error_input_key} `{error_input_value}` is an invalid language, please check."


async def error_handler(request: Request, exc: InvalidLanguageError):
    return JSONResponse(status_code=exc.code, content={"error": {"name": exc, "message": exc.message}},)


def load_exception_handler(app):
    exception_list = [InvalidLanguageError]
    for exec in exception_list:
        app.add_exception_handler(exec, error_handler)
