import streamlit as st
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate


# Load environment variables
load_dotenv()


# Model setup
llm = HuggingFaceEndpoint(
    model="Qwen/Qwen3.8-2.4T-A95B"
)

model = ChatHuggingFace(llm=llm)


# Prompt setup
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Extract useful information from the given paragraph. Do not invent facts."
    ),
    (
        "human",
        "{paragraph}"
    )
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
            "paragraph": paragraph
        })

        response = model.invoke(final_prompt)

        st.subheader("Extracted Information")
        st.write(response.content)
