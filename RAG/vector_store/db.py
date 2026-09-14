from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_docling.loader import DoclingLoader
from langchain_chroma import Chroma

load_dotenv()

FILE_PATH = "RAG/document_loaders/resume.pdf"
data = DoclingLoader(FILE_PATH)
docs = data.load()

for doc in docs:
    doc.metadata = {
        "source": doc.metadata.get("origin", {}).get("filename", "unknown"),
    }

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma-db"
)

result = vectorstore.similarity_search("Project", k=3)

for r in result :
    print(r)