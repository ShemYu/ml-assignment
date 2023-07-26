from typing import List

from pydantic import BaseModel


class Record(BaseModel):
    id: str
    text: str


class Payload(BaseModel):
    fromLang: str
    records: List[Record]
    toLang: str


class TranslationRequest(BaseModel):
    payload: Payload


class TranslationResponse(BaseModel):
    result: List[Record]
