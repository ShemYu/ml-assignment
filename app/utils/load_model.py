import torch
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

model = None
tokenizer = None
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

async def load_model():
    """
    Asynchronously loads the M2M100 model and tokenizer from the pretrained
    `facebook/m2m100_418M` package if not already loaded.

    Returns:
        model (M2M100ForConditionalGeneration): The loaded M2M100 model.
        tokenizer (M2M100Tokenizer): The loaded M2M100 tokenizer.
        device (torch.device): The device (either "cuda" if available, or "cpu") where the model will be run.
    """
    global model, tokenizer
    if model is None:
        model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
        model.to(device)
    if tokenizer is None:
        tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
    return model, tokenizer, device
