from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# temprature refers to how creative the answer is, its value ranges from 0 to 2.

# max_completion_token can be seen as maximum number of words which we want in the answer.

model = ChatOpenAI(model = 'gpt-4', temperature=0, max_completion_tokens=10)

result = model.invoke("What is the Capital of India?")

print(result)