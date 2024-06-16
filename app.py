import os
from dotenv import load_dotenv
import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from helper import response_generator
from prompt import CUSTOM_QUESTION_PROMPT

load_dotenv(".env")
GROQ_KEY = os.getenv("GROQ_KEY")

chat = ChatGroq(temperature=0.7, groq_api_key=GROQ_KEY,
                model_name="llama3-8b-8192")


if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    chat_name = st.text_input("Input a chat name")
    create_chat_button = st.button(
        "New", use_container_width=True, key="create_chat_button")

    if create_chat_button:
        if chat_name:
            st.session_state.messages.append({chat_name: []})
        else:
            st.warning("Input a chat name")

    current_chat = st.radio(
        label="Conversation",
        options=[key for d in st.session_state.messages for key in d.keys()],
        label_visibility="collapsed",
        index=0,
        key="current_chat"
    )

if current_chat:
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)

    conversational_chain = LLMChain(
        llm=chat,
        prompt=CUSTOM_QUESTION_PROMPT,
        memory=memory
    )

    prompt = st.chat_input("Say something")
    if prompt:
        for page in st.session_state.messages:
            if current_chat in page:
                page[current_chat].append({"role": "user", "content": prompt})
                response = response_generator(conversational_chain, prompt)
                page[current_chat].append(
                    {"role": "assistant", "content": response})

    for page in st.session_state.messages:
        if current_chat in page:
            for message in page[current_chat]:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])


else:
    st.warning("Please create a Conversation to start")
