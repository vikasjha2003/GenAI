from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large' , dimensions=32)

documents = [
    "Vikas", "Kumar", "Jha"
]

result = embedding.embed_documents(documents)

print(str(result))