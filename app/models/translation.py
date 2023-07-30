from typing import List

from pydantic import BaseModel, Field


class Record(BaseModel):
    id: str = Field(..., description="Unique identifier for each record")
    text: str = Field(..., description="The text to be translated")


class TranslationPayload(BaseModel):
    fromLang: str = Field(..., description="Source language code (e.g., 'en' for English)")
    toLang: str = Field(..., description="Target language code (e.g., 'ja' for Japanese)")
    records: List[Record] = Field(..., description="List of records to be translated")


class TranslationRequest(BaseModel):
    payload: TranslationPayload = Field(..., description="Payload containing all necessary details for the translation request")

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
    result: List[Record] = Field(..., description="List of records containing the translation results")

    class Config:
        json_schema_extra = {"example": {"result": [{"id": "123", "text": "人生はチョコレートの箱のようなものだ。"}],}}
