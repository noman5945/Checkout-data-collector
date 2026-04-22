from ..interfaces.ocr_interface import OCRInterface

class GoogleOCR(OCRInterface):
    async def extractTexts(self, image):
        return await super().extractTexts(image)