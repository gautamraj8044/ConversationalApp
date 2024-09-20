import streamlit as st
from transformers import pipeline
import torch
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Check if GPU is available
device = 0 if torch.cuda.is_available() else -1

# Initialize Hugging Face model for text generation on GPU (if available)
chat_model = pipeline("text-generation", model="google/flan-t5-large", device=device)  # device=0 for GPU, device=-1 for CPU

# StreamLit UI settings
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hey, I'm your Chat GPT")

# Initialize session state for messages if not already present
if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# Function to generate an answer using the Hugging Face model
def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    
    # Generate response using Hugging Face model
    assistant_answer = chat_model(question, max_length=50, num_return_sequences=1)[0]['generated_text']
    
    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer))
    
    return assistant_answer

# Get user input
def get_text():
    input_text = st.text_input("You: ", key='input_text')
    return input_text

# Input and button for submission
user_input = get_text()
submit = st.button('Generate')

if submit:
    response = load_answer(user_input)
    st.subheader("Answer:")
    st.write(response, key=1)
