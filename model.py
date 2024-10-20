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
history = []