
import streamlit as st
import requests

API_KEY = st.secrets["YOUTUBE_API_KEY"]
st.title("Busca de Vídeos por Hashtag no YouTube")

query = st.text_input("Digite a hashtag (sem #):")

if query:
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q=%23{query}&type=video&key={API_KEY}&maxResults=5"
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        for item in data["items"]:
            st.subheader(item["snippet"]["title"])
            st.write(f"https://www.youtube.com/watch?v={item['id']['videoId']}")
            st.write(item["snippet"]["description"])
    else:
        st.warning("Nenhum vídeo encontrado ou erro na API.")
