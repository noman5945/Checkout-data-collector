from abc import ABC,abstractmethod

class OCRInterface(ABC):

    @abstractmethod
    async def extractTexts(self,image:bytes):
        pass