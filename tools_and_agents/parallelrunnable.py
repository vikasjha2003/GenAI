from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda

# model
model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

# prompt
prompt1 = ChatPromptTemplate.from_template("Explain {topic} briefly")
prompt2 = ChatPromptTemplate.from_template("Explain {topic} in 2 points only")

# output parser
parser = StrOutputParser()

chain = RunnableParallel({
    "one" : RunnableLambda(lambda x : x['one']) | prompt1 | model | parser,
    "two" : RunnableLambda(lambda x : x['two']) | prompt2 | model | parser
})

result = chain.invoke({
    "one" : {"topic" : "Thread"},
    "two" : {"topic" : "Process"}
})

print(result["one"])
print(result["two"])