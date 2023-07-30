import torch
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer


model = None
tokenizer = None
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


async def load_model():
    global model, tokenizer
    if model == None:
        model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
        model.to(device)
    if tokenizer == None:
        tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
    return model, tokenizer, device
