import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.embeddings import FakeEmbeddings
import anthropic

load_dotenv()

CHROMA_DIR = "data/chroma_db"

def get_answer(question: str) -> str:
    embeddings = FakeEmbeddings(size=384)
    vectorstore = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )

    docs = vectorstore.similarity_search(question, k=4)
    context = "\n\n".join([doc.page_content for doc in docs])

    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a helpful assistant that answers questions about CMS Medicare and Medicaid policy documents.

Use the following context excerpts to answer the question. If the context doesn't contain enough information, say so clearly.

Context:
{context}

Question: {question}

Answer:"""
            }
        ]
    )

    return message.content[0].text

if __name__ == "__main__":
    question = "What is the methodology used for Medicare Monthly Enrollment calculations?"
    print(f"Question: {question}\n")
    answer = get_answer(question)
    print(f"Answer:\n{answer}")
