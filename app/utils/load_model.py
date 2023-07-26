from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer


model = None
tokenizer = None


async def load_model():
    global model, tokenizer
    if model == None:
        model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
    if tokenizer == None:
        tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M", src_lang="en", tgt_lang="fr")
    return model, tokenizer


if __name__ == "__main__":
    load_model()
