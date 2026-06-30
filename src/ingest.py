import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

RAW_DATA_DIR = "data/raw"

def load_and_chunk_documents():
    all_chunks = []
    pdf_files = [f for f in os.listdir(RAW_DATA_DIR) if f.endswith(".pdf")]

    print(f"Found {len(pdf_files)} PDF files to process.\n")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    for filename in pdf_files:
        filepath = os.path.join(RAW_DATA_DIR, filename)
        print(f"Loading: {filename}")
        loader = PyPDFLoader(filepath)
        pages = loader.load()
        chunks = splitter.split_documents(pages)
        all_chunks.extend(chunks)
        print(f"  -> {len(pages)} pages, {len(chunks)} chunks\n")

    print(f"Total chunks across all documents: {len(all_chunks)}")
    return all_chunks

if __name__ == "__main__":
    chunks = load_and_chunk_documents()
