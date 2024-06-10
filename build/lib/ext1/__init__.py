from .extraction import (
    PageInfo,
    ExtractionOutput,
    DocInterface,
    ExtractionEvent,
    process_info,
    ExtractionExample
)

def process_extraction(doc_info, doc_reader):
    extraction_example = ExtractionExample()
    extraction_example.on_doc_data(doc_info, doc_reader)
