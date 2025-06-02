import streamlit as st

from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# Load API keys from environmentcd "C:\Users\aditi\OneDrive\web development\clauseai"
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    os.environ["GROQ_API_KEY"] = api_key

# Initialize models
groq_model = ChatGroq(model="llama3-8b-8192")

# Prompts
essay_prompt = ChatPromptTemplate.from_template("Write me an essay about {topic} with 150 words.")
poem_prompt = ChatPromptTemplate.from_template("Write me a poem about {topic} with 150 words.")

st.title("ClauseAI: Essay and Poem Generator")

topic = st.text_input("Enter the topic")

choice = st.radio("Choose type", ("Essay", "Poem"))

if st.button("Generate"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        if choice == "Essay":
            prompt = f"Write me an essay about {topic} with 150 words."
            response = groq_model.invoke(prompt)
            st.subheader("Essay:")
            st.write(response.content)
        else:
            prompt = f"Write me a poem about {topic} with 150 words."
            response = groq_model.invoke(prompt)
            st.subheader("Poem:")
            st.write(response.content)
    # Show additional content about the topic
    st.markdown("---")
    st.markdown(f"You searched for: {topic}")
    st.info(f"For more information about '{topic}', contact us at your.email id")

# streamlit run clauseai/main.py



