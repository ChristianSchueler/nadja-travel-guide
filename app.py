import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Travel Guide",
    page_icon="✈️",
    layout="wide"
)

# Title
st.title("AI Travel Guide")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What would you like to know about your travel destination?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # TODO: Implement LangChain/LangGraph logic here
            response = f"I'll help you explore {prompt}"
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
