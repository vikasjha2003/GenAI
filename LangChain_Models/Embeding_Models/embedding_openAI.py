from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large' , dimensions=32)

result = embedding.model_query("Vikas Kumar Jha")

print(str(result))