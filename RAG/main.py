from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma

# vector store

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma(
    persist_directory="chroma-db",
    embedding_function=embedding_model
)

# Retrieval

mmr_retriever = vector_store.as_retriever(
    search_type = "mmr",
    search_kwargs = {
        "k" : 4,
        "fetch_k":8,
        "lambda_mult" :0.5
    }
)


# Setting up Model

llm = HuggingFaceEndpoint(
    model="Qwen/Qwen3-8B"
)

model = ChatHuggingFace(llm=llm)

# Prompt generation

prompt_template = ChatPromptTemplate([
    ("system","You summarize the text and answer only based on the data.") , 
    ("human","{data}")
])

# final execution

query = input("What to Summarize? -> ")
docs = mmr_retriever.invoke(query)

prompt = prompt_template.format_messages(data = docs)

result = model.invoke(prompt)
print(result.content)