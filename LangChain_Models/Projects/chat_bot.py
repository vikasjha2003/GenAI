import streamlit as st

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model="deepseek-ai/DeepSeek-V4-Flash-0731"
)

model = ChatHuggingFace(llm=llm)

# Store messages in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a Ninja from Naruto universe")
    ]

st.title("🥷 Naruto Ninja Chat")
st.caption("Chat with a Ninja from the Naruto universe")

# Display conversation
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Chat input
prompt = st.chat_input("You : ")

if prompt:
    # Add and display user message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Get model response
    response = model.invoke(st.session_state.messages)

    # Add and display AI response
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant"):
        st.write(response.content)

# Display conversation below the chat
st.divider()
st.subheader("Conversation")

for message in st.session_state.messages:
    st.write(message)