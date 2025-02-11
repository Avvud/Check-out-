import streamlit as st

# App Title
st.title("📝 Simple Text Analyzer")

# Sidebar
st.sidebar.header("Settings")
user_text = st.text_area("Enter your text here:"
