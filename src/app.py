# src/app.py
import streamlit as st
import sys
import os

# Añadir el directorio 'src' al path para los imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from chatbot import ChatMate
from utils import format_message

st.set_page_config(page_title="ChatMate 🤖", page_icon="🤖", layout="wide")
st.title("ChatMate 🤖 - Tu asistente inteligente")

chatbot = ChatMate()

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Escribe tu mensaje aquí:")

if user_input:
    response = chatbot.get_response(user_input)
    st.session_state.history.append(("Tú", user_input))
    st.session_state.history.append(("Bot", response))

for sender, message in st.session_state.history:
    st.markdown(format_message(sender, message))