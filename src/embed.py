import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from langchain_chroma import Chroma
from langchain_community.embeddings import FakeEmbeddings
from ingest import load_and_chunk_documents

CHROMA_DIR = "data/chroma_db"

def build_vector_store():
    print("Loading and chunking documents...")
    chunks = load_and_chunk_documents()

    print("\nGenerating embeddings and storing in Chroma...")
    embeddings = FakeEmbeddings(size=384)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )

    print(f"\nDone! {len(chunks)} chunks stored in {CHROMA_DIR}")
    return vectorstore

if __name__ == "__main__":
    build_vector_store()
