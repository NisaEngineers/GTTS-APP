# app.py
import streamlit as st
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Text to Speech 🎙️", page_icon="🎧", layout="centered")

# --- UI Styling ---
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: #fafafa;
    }
    .stTextArea textarea {
        background-color: #1c1f26;
        color: #fafafa;
        border-radius: 10px;
    }
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1c1f26;
        color: #fafafa;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4f46e5;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #4338ca;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- App Title ---
st.title("🎙️ Text to Speech with gTTS")
st.write("Type your text, choose a language, and generate natural speech instantly.")

# --- Input ---
text = st.text_area("Enter text:", height=150, placeholder="Type something here...")
lang = st.selectbox(
    "Language:",
    ["en", "bn", "hi", "fr", "de", "es", "it", "pt", "ja", "ko", "zh-cn", "ar", "ru"],
    index=0,
)

# --- Generate Speech ---
if st.button("🔊 Convert to Speech"):
    if text.strip():
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tts.save(tmp.name)
            audio_path = tmp.name

        st.success("✅ Speech generated successfully!")
        st.audio(audio_path, format="audio/mp3")

        with open(audio_path, "rb") as f:
            st.download_button(
                label="⬇️ Download MP3",
                data=f,
                file_name="speech.mp3",
                mime="audio/mp3",
            )

        # Clean up temp file after download
        os.remove(audio_path)
    else:
        st.error("⚠️ Please enter some text before converting.")
