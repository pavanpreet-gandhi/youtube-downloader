import logging
import streamlit as st
from src import download_youtube_video


def app():

    st.title('Download a YouTube video')
    youtube_url = st.text_input('Enter the YouTube URL')
    fetch_button = st.button('Fetch YouTube Video')

    # Create a placeholders for the fetching message and download button
    fetching_message_placeholder = st.empty()
    download_button_placeholder = st.empty()

    if fetch_button and youtube_url:

        # Display a fetching message
        fetching_message_placeholder.text('Fetching YouTube video...')

        # Fetch the YouTube video and convert it to MP3
        try:
            title = download_youtube_video(url=youtube_url, output_dir='audio')
        
        # Handle exceptions
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            fetching_message_placeholder.text('YouTube URL is invalid or the video is not available. Please try again.')
            return

        # Read the file data
        with open('audio/audio.mp3', 'rb') as f:
            file_data = f.read()

        # Replace the placeholder with the download button
        download_button_placeholder.download_button(
            label = 'Download MP3',
            data = file_data,
            file_name = title.lower().replace(' ', '-')+'.mp3',
            mime = 'audio/mpeg',
        )


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    app()