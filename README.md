# 📘 Smart Ebook Reader

Smart Ebook Reader is an **AI-powered learning-focused PDF reader** that allows users to read ebooks and documents while instantly understanding words through a contextual popup dictionary — without breaking the reading flow.

Unlike traditional PDF readers, this app is designed for **students, English learners, and exam aspirants**.

---

## 🚀 Key Features

### 📄 Advanced PDF Reading
- High-quality PDF rendering (near Adobe / Google Drive quality)
- Native text selection, copy, and highlight
- Zoom controls with quality lock (no blur)
- Page navigation (Next / Previous)
- Night mode for comfortable reading

### 🧠 Smart Word Popup (Core Feature)
- Select any word inside a PDF
- Instant popup with:
  - Meaning
  - Part of Speech (Grammar)
  - Example sentence
  - Synonyms
  - Antonyms
  - Pronunciation audio
- Works **without OCR for text PDFs**

### 🖼️ OCR Support (Images Only)
- OCR is applied **only for image-based documents**
- Extracted text becomes selectable
- Same popup dictionary works for OCR text

### ⭐ Highlights & Learning
- Save highlighted words
- Persistent highlights per book & page
- Designed for vocabulary building and comprehension

### 📱 App Ready
- Web app + Flutter app (WebView-based)
- Can be distributed as APK (no Play Store required initially)
- Monetization-ready (AdMob / Premium features)

---

## 🛠️ Tech Stack

### Frontend
- HTML, CSS, JavaScript
- PDF.js (Canvas + TextLayer)
- High-DPI rendering for better quality

### Backend
- FastAPI (Python)
- NLTK (WordNet)
- spaCy (Grammar / POS)
- Tesseract OCR (Images only)

### Mobile App
- Flutter
- WebView (wraps web app)
- Android-ready

---

## 📂 Project Structure

smart-ebook-reader/
│
├── backend/
│ ├── main.py
│ ├── nlp.py
│ └── requirements.txt
│
└── frontend/
└── index.html


---

## ⚙️ Setup Instructions

### 1️⃣ Backend Setup
```bash
cd backend
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000

2️⃣ Frontend Setup

Open frontend/index.html in a browser

Upload a PDF or image

Select any word to see the popup dictionary
