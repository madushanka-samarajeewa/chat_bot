import streamlit as st
import numpy as np
import random
import time

from query_data import query_rag

st.title("WiCof Bot")


# with st.chat_message("user"):

#     st.write("Hello  👋")

# with st.chat_message("assistant"):

#     st.write("Hello user ,am a chatbot")
    
# prompt = st.chat_input("Say Something")

# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")

# Streamed response emulator
def response_generator():
    # response = random.choice(
    #     [
    #         "Hello there! How can I assist you today?",
    #         "Hi, human! Is there anything I can help you with?",
    #         "Do you need help?",
    #     ]
    # )

    response = query_rag(prompt)

    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())

    # #response = f"Echo: {prompt}"
    # # Display assistant response in chat message container
    # with st.chat_message("assistant"):
    #     st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})