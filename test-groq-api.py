print("Loading dependencies...")

from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq
import os

# Load environment variables
load_dotenv()

print("Connecting to Groq...")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
print("Connected to Groq")

# Ask a simple question
question = "What is the capital of Finland?"

# Construct a simple prompt
prompt = (
    f"You are a helpful assistant.\n"
    f"Answer the following question clearly and concisely:\n\n"
    f"Question: {question}\n"
    f"Answer:"
)

print("Asking question...")
# Get the response from the model
response = groq_llm.invoke(prompt)
print("Response received")

# Print the response
print(response.content.strip())