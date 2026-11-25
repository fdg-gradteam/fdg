# OCR (Google Cloud Vision)

A small web app that extracts text from uploaded images and PDF files using
Google Cloud Vision `document_text_detection` (Arabic + English).

- **Images:** PNG, JPG, WEBP, TIFF, BMP, GIF
- **PDF:** each page is rendered to an image with PyMuPDF, then sent to Vision
- Up to 25 MB per upload; several files at once
- Copy or download the result as `.txt`

## Setup

1. Put your Google Cloud service-account key (`.json`) inside this `ocr/` folder.
   It is picked up automatically and is ignored by Git (see `ocr/.gitignore`).
   Alternatively set `GOOGLE_APPLICATION_CREDENTIALS` to the key's path.
2. Install and run:

```bash
pip install -r requirements.txt
python app.py
```

3. Open http://localhost:5000

## API

`POST /api/ocr` with multipart field `files` (one or more). Returns:

```json
{"results": [{"filename": "a.pdf", "text": "...", "pages": [{"page": 1, "text": "..."}]}]}
```

A file that fails returns `{"filename": "...", "error": "..."}` instead.
