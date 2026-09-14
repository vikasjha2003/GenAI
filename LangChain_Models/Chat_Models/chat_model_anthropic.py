from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

# won't work since no API key ahas been set in dotenv file for anthropic, this is also a paid model 

model = ChatAnthropic(model='claude-3.5-sonet-20241022')

result = model.invoke("What if the Capital of Haryana?")

print(result)