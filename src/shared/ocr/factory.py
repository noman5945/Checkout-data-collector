from .providers.google_ocr import GoogleOCR
from .config import OCR_PROVIDER

def get_ocr():
    if OCR_PROVIDER == "google":
        return GoogleOCR()

    raise Exception("Invalid OCR provider")