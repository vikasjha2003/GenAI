# load PDF -> Split into Chunks -> Create Embeddings -> store into Chroma

# imports
from langchain_unstructured import UnstructuredLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from dotenv import load_dotenv
load_dotenv()

# Document Loader

FILE_PATH = "RAG/document_loaders/resume.pdf"
data = UnstructuredLoader(file_path=FILE_PATH)
docs = data.load()

for doc in docs:
    doc.metadata = {
        "source": doc.metadata.get("origin", {}).get("filename", "unknown"),
    }

# Text Splitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500, chunk_overlap = 100
)
chunks = splitter.split_documents(docs)

# Embedding

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma-db"
)