import streamlit as st

def generate_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a program, but thanks for asking!"
    else:
        return "I'm sorry, I don't understand that question."

st.set_page_config(page_title="AI Chatbot", page_icon=":shark:")

st.title("AI Chatbot")

user_input = st.text_input("Ask me anything...", "")
send_btn = st.button("Send Message")

if user_input and send_btn:
    response = generate_response(user_input)
    st.code(response)
