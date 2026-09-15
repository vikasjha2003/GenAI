from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)

parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({"topic" : "Anime"})

print(result)

# Below stuff is not needed thanks to runnable

# final_prompt = prompt.format_messages(topic="Output Parser")

# response = model.invoke(final_prompt)

# final_output = parser.parse(response.content)

# print(final_output)