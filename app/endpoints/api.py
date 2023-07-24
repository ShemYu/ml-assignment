from fastapi import FastAPI

app = FastAPI()


@app.post("/translation")
def translation(src_text: str, target_lang: str):
    return {"result": "The target."}
