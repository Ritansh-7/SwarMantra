import streamlit as st
import requests

# API Details for Llama
API_KEY = "LA-fa24fb30b9104bf39c59a45fe2702b768c87e6e979e84d7facff6683747b7dcf"
BASE_URL = "https://api.llama-api.com"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Generate song lyrics using Llama API
def generate_song(theme, genre, mood, language="English"):
    prompt = f"Write a {genre} song about {theme} with a {mood} tone in {language}. Include verses and a chorus."
    payload = {
        "messages": [
            {"role": "system", "content": "You are a creative songwriter AI."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1200
    }

    response = requests.post(f"{BASE_URL}/chat/completions", headers=HEADERS, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit UI
st.title("🎵 SwarMantra AI 🎤")
st.write("Generate custom songs based on theme, genre, and mood!")

theme = st.text_input("Enter a song theme (love, adventure, heartbreak, etc.)")
genre = st.selectbox("Select a genre", ["Pop", "Rock", "Rap", "Jazz", "Lofi", "Metal"])
mood = st.selectbox("Select a mood", ["Happy", "Sad", "Energetic", "Relaxing", "Motivational"])
language = st.selectbox("Select a language", ["English", "Hindi"])

if st.button("Generate Song 🎼"):
    if theme:
        with st.spinner("Generating song lyrics..."):
            lyrics = generate_song(theme, genre, mood, language)
            st.text_area("🎶 Enjoy the lyrics and melody:", lyrics, height=300)
    else:
        st.warning("Please enter a theme to generate lyrics.")
