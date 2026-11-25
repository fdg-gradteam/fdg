import os
from pathlib import Path

from flask import Flask, jsonify, render_template, request
from google.cloud import vision

BASE_DIR = Path(__file__).resolve().parent

# Use the service-account key in this folder unless one is already configured.
if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
    keys = sorted(BASE_DIR.glob("*.json"))
    keys = [k for k in keys if k.name not in ("package.json",)]
    if keys:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(keys[0])

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024  # 25 MB per request

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".tif", ".tiff", ".ico"}
PDF_EXT = {".pdf"}

_client = None


def get_client():
    global _client
    if _client is None:
        _client = vision.ImageAnnotatorClient()
    return _client


def detect_text_bytes(content: bytes) -> str:
    """Run dense-text OCR (document_text_detection) on image bytes."""
    image = vision.Image(content=content)
    response = get_client().document_text_detection(
        image=image,
        image_context=vision.ImageContext(language_hints=["ar", "en"]),
    )
    if response.error.message:
        raise RuntimeError(
            f"{response.error.message}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors"
        )
    # full_text_annotation holds the whole text once, in reading order.
    # (text_annotations[0] is the same text; the rest are single words.)
    if response.full_text_annotation and response.full_text_annotation.text:
        return response.full_text_annotation.text
    if response.text_annotations:
        return response.text_annotations[0].description
    return ""


def pdf_to_images(content: bytes, zoom: float = 2.0):
    """Render each PDF page to PNG bytes."""
    import pymupdf as fitz

    with fitz.open(stream=content, filetype="pdf") as doc:
        for page in doc:
            pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
            yield pix.tobytes("png")


def ocr_file(filename: str, content: bytes):
    ext = Path(filename).suffix.lower()
    if ext in PDF_EXT:
        pages = []
        for i, img in enumerate(pdf_to_images(content), start=1):
            pages.append({"page": i, "text": detect_text_bytes(img)})
        return pages
    if ext in IMAGE_EXT:
        return [{"page": 1, "text": detect_text_bytes(content)}]
    raise ValueError(f"نوع الملف غير مدعوم: {ext or 'بدون امتداد'}")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/ocr", methods=["POST"])
def api_ocr():
    files = request.files.getlist("files")
    if not files:
        return jsonify({"error": "لم يتم رفع أي ملف"}), 400

    results = []
    for f in files:
        item = {"filename": f.filename}
        try:
            pages = ocr_file(f.filename, f.read())
            item["pages"] = pages
            item["text"] = "\n\n".join(p["text"] for p in pages)
        except Exception as e:  # report per-file errors, keep going
            item["error"] = str(e)
        results.append(item)
    return jsonify({"results": results})


@app.errorhandler(413)
def too_large(_):
    return jsonify({"error": "حجم الملفات أكبر من 25 ميجابايت"}), 413


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
