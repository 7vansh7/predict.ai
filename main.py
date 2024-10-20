import streamlit as st
import sys
sys.path.append('./')
from model import llm, history,chat

st.set_page_config(page_title="Psychologist", layout="centered")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


psy_prompt = """You name is Aura, you are a psychologist, An EXPERET in 
PREDICTING HUMAN BEHAVIOUR by making lots of Assumptions.
You are adept in psychology, philosophy, and literature.
Ask questions from the user to better your analysis and answer.
Give examples from contemporary studies if required.
You give people psychological help and also help them predicting other 
people's behaviour.
Give ANALYSIS in TABULAR FORMAT with the PROBABLITY of things happening if required.
Talk like a HUMAN PSYCHOLOGIST.
Give a good initial response 
Use Underlines and bold when answering 
"""

if len(st.session_state['chat_history']) == 0:
    initial_response = chat.send_message(psy_prompt).text
    st.session_state['chat_history'].append({"user": "Aura", "message": initial_response})

with st.sidebar:
    st.title("AI Psychologist")
    st.markdown("Get quick answers to your psychological needs and predict other people's behaviour. Not for medical use.")
    st.markdown('[Want an AI Model for you business, Click here ](https://www.linkedin.com/company/discourseaihome/?viewAsMember=true)')
    st.text_area(label='Write any thoughts here')

st.title("Welcome to the Chat!")

chat_box = st.container()

def add_message(user, message):
    st.session_state['chat_history'].append({"user": user, "message": message})

def send_message():
    user_message = st.session_state.user_input  # Access user input from session state
    if user_message:
        add_message("You", user_message)
        # chat = llm.start_chat(history=history)
        res = chat.send_message(user_message,).text
        add_message("Aura", res)
        st.session_state.user_input = ""  # Clear input field after submission

# Text input for the user's message with key assigned
user_message = st.text_input("Your message", "", key="user_input", on_change=send_message)

bubble_style = """
<style>
.chat-bubble {
    padding: 10px;
    border-radius: 15px;
    margin-bottom: 10px;
    max-width: 80%;
    word-wrap: break-word;
    color: black;
}
.user-bubble {
    background-color: #DCF8C6;
    text-align: left;
    margin-left: auto;
}
.bot-bubble {
    background-color: #E0E0E0;
    text-align: left;
    margin-right: auto;
}
.chat-container {
    display: flex;
    flex-direction: column;
}
</style>
"""

st.markdown(bubble_style, unsafe_allow_html=True)

with chat_box:
    for entry in st.session_state['chat_history']:
        user = entry['user']
        message = entry['message']

        if user == "You":
            st.markdown(f'<div class="chat-bubble user-bubble">{user}: {message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble bot-bubble">{user}: {message}</div>', unsafe_allow_html=True)
