import streamlit as st
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if api_key:
    os.environ["GROQ_API_KEY"] = api_key

groq_model = ChatGroq(model="llama3-8b-8192")

st.title("ClauseAI: Chatbot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")

# User input
user_input = st.text_input("Type your message and press Enter:", key="user_input")

if st.button("Send") or (user_input and st.session_state.get("user_input_submitted", False)):
    if user_input.strip():
        st.session_state["messages"].append({"role": "user", "content": user_input})
        # Get response from Groq model
        response = groq_model.invoke(user_input)
        st.session_state["messages"].append({"role": "bot", "content": response.content})
        # st.experimental_rerun()  # Removed for compatibility with your Streamlit version
    else:
        st.warning("Please enter a message.")