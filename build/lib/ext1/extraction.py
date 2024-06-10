from dataclasses import dataclass
from abc import ABC, abstractmethod
import numpy as np

@dataclass
class PageInfo:
    words: list
    cords: list
    ocr_type: str
    width: int
    height: int
    image: np.ndarray

@dataclass
class ExtractionOutput:
    data: dict

class DocInterface(ABC):
    @abstractmethod
    def load_page(self, page_num: int) -> PageInfo:
        pass

    @abstractmethod
    def page_count(self) -> int:
        pass

class ExtractionEvent(ABC):
    @abstractmethod
    def on_doc_data(self, doc_info, reader: DocInterface) -> ExtractionOutput:
        pass

def process_info():
    print('I can process')

class ExtractionExample(ExtractionEvent):
    def on_doc_data(self, doc_info, doc_reader):
        print('Got data for extraction event')
        process_info()
