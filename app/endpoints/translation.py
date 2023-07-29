from typing import List

from fastapi import APIRouter

from app.models.translation import Record, TranslationRequest, TranslationResponse
from app.utils.exception_handler import InvalidLanguageError
from app.utils.load_model import load_model


router = APIRouter(prefix="/translation")


@router.post("/", response_model=TranslationResponse)
async def translation(request_body: TranslationRequest):
    # src_text = "Life is like a box of chocolates."
    # tgt_lang = "人生はチョコレートの箱のようなものだ。"
    model, tokenizer = await load_model()
    try:
        tokenizer.src_lang = request_body.payload.fromLang
    except KeyError:
        raise InvalidLanguageError(error_input_key="fromLang", error_input_value=request_body.payload.fromLang)
    to_lang = request_body.payload.toLang
    result_records: List[Record] = []

    for record in request_body.payload.records:
        model_inputs = tokenizer(record.text, return_tensors="pt")
        try:
            generated_tokens = model.generate(**model_inputs, forced_bos_token_id=tokenizer.get_lang_id(to_lang))
        except KeyError as e:
            raise InvalidLanguageError(error_input_key="toLang", error_input_value=to_lang)
        result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        result_records.append(Record(id=record.id, text=result[0]))
    return TranslationResponse(result=result_records)
