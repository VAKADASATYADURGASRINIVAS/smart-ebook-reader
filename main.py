from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from nlp import get_word_data
from PIL import Image
import pytesseract

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"status": "API running"}

@app.get("/define")
def define(word: str):
    # 🛡️ SAFETY: remove junk symbols
    word = ''.join(c for c in word if c.isalpha())
    if not word:
        return {
            "word": "",
            "meaning": "Meaning not found",
            "pos": "",
            "synonyms": [],
            "antonyms": [],
            "examples": [],
            "pronunciation": ""
        }
    return get_word_data(word.lower())

# OCR ONLY FOR IMAGES (NOT PDFs)
@app.post("/ocr-image")
async def ocr_image(file: UploadFile = File(...)):
    img = Image.open(file.file)
    text = pytesseract.image_to_string(img)
    return {"text": text}
