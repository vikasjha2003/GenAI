from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = [
    "Vikas", "Kumar" , "Jha"
]

vector = embedding.embed_documents(text)

print(str(vector))