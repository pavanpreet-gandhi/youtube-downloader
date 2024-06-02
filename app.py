import streamlit as st
from src import download_youtube_video

def app():
    st.title("Download a YouTube video")
    youtube_url = st.text_input("Enter the YouTube URL")
    download_button = st.button("Download")

    if download_button:
        download_youtube_video(url=youtube_url, output_dir='audio')
        st.write("Download complete!")

if __name__ == "__main__":
    app()