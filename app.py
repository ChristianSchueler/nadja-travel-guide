import streamlit as st
from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Nadja AI Travel Guide",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("✈️ Nadja AI Travel Guide")

# Sidebar layout
with st.sidebar:
    st.title("🛠 Settings")

    # Initialize session state for the model if it doesn't exist
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "llama-3.1-8b-instant"

    model_list = [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
        "llama3-70b-8192",
        "llama3-8b-8192",
        "mixtral-8x7b-32768",
        "gemma2-9b-it"
    ]

    st.session_state.selected_model = st.selectbox(
        "🤖 Select Model",
        model_list,
        key="model_selector",
        index=model_list.index(st.session_state.selected_model)
    )

    reset_button = st.button("🔄 Reset Conversation", key="reset_button")
    if reset_button:
        st.session_state.messages = []

# Initialize the LLM for the first time
model_name = st.session_state.selected_model
st.session_state.current_model = model_name
st.session_state.llm = ChatGroq(model=model_name, temperature=0.5)
print(f"Using model: {model_name}")

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
            response = st.session_state.llm.invoke(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
