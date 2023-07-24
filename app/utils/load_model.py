from transformers import M2M100Config, M2M100ForConditionalGeneration, M2M100Tokenizer

def load_model():
    model = M2M100ForConditionalGeneration.from_pretrained('facebook/m2m100_418M')
    tokenizer = M2M100Tokenizer.from_pretrained('facebook/m2m100_418M', src_lang="en", tgt_lang="fr")
    return model, tokenizer

if __name__ == "__main__":
    load_model()
