from typing import List

from pydantic import BaseModel, Field


class Record(BaseModel):
    id: str = Field(...)
    text: str = Field(...)


class TranslationPayload(BaseModel):
    fromLang: str = Field(...)
    toLang: str = Field(...)
    records: List[Record] = Field(...)


class TranslationRequest(BaseModel):
    payload: TranslationPayload = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "payload": {
                    "fromLang": "en",
                    "records": [{"id": "123", "text": "Life is like a box of chocolates."}],
                    "toLang": "ja",
                }
            }
        }


class TranslationResponse(BaseModel):
    result: List[Record]

    class Config:
        json_schema_extra = {
            "example": {
                "result": [{"id": "123", "text": "人生はチョコレートの箱のようなものだ。"}],
            }
        }
