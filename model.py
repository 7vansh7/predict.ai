import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  }
]
genai.configure(api_key=st.secrets['GOOGLE_API_KEY'])
llm = genai.GenerativeModel(model_name='gemini-1.5-flash-002',safety_settings=safety_settings)
chat = llm.start_chat(history=[])
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
initial_response = chat.send_message(psy_prompt).text