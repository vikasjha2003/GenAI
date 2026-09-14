import streamlit as st
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List,Optional


# Load environment variables
load_dotenv()


# Model setup
llm = HuggingFaceEndpoint(
    model="Qwen/Qwen3.8-2.4T-A95B"
)

model = ChatHuggingFace(llm=llm)


# Prompt setup


class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str



parser = PydanticOutputParser(pydantic_object=Movie)


prompt = ChatPromptTemplate.from_messages([
    ('system',"""
Extract movie information from the paragraph
     {format_instructions}
"""), ("human","{paragraph}")
])


# Streamlit UI
st.title("Information Extraction")

paragraph = st.text_area(
    "Give your paragraph:",
    height=250,
    placeholder="Enter your paragraph here..."
)

if st.button("Extract Information"):
    if paragraph:
        final_prompt = prompt.invoke({
            "paragraph" : paragraph,
            "format_instructions": parser.get_format_instructions()
            
        })

        response = model.invoke(final_prompt)
        movie_data = parser.parse(response.content)

        st.subheader("Extracted Information")
        st.write(movie_data)