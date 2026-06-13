from utils.document_loader import load_documents
from utils.text_splitter import split_documents
from utils.embeddings import get_embeddings

from langchain_community.vectorstores import FAISS

print("Loading documents...")

documents = load_documents("documents")

print("Splitting documents...")

chunks = split_documents(documents)

print("Generating embeddings...")

embeddings = get_embeddings()

print("Creating FAISS vector database...")

db = FAISS.from_documents(
    chunks,
    embeddings
)

db.save_local("vector_db")

print("Vector DB created successfully!")