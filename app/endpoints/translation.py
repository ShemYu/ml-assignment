from fastapi import APIRouter

from app.models.translation import TranslationRequest, TranslationResponse
from app.utils.load_model import load_model


router = APIRouter(prefix="/translation")


@router.post("/", response_model=TranslationResponse)
async def translation(request_body: TranslationRequest):
    src_text = "Life is like a box of chocolates."
    tgt_lang = "人生はチョコレートの箱のようなものだ。"
    model, tokenizer = await load_model()
    tokenizer.src_lang = "en"
    model_inputs = tokenizer(src_text, return_tensors="pt")
    generated_tokens = model.generate(**model_inputs, forced_bos_token_id=tokenizer.get_lang_id("ja"))
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return TranslationResponse(result=[{"id": "123", "text": result[0]}])
