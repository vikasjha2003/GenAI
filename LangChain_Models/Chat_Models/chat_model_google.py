from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# another closed source model, not usable for free.

# code is incomplete, fill in the blanks yourself

load_dotenv()

model = ChatGoogleGenerativeAI(model='')

result = model.invoke()

print(result)