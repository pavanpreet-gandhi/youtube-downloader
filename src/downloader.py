from pathlib import Path
from pytube import YouTube
import subprocess
import logging

def download_youtube_video(url, output_dir):
    """
    Downloads a YouTube video as an mp3 file.

    Parameters:
        - url (str): The URL of the YouTube video.
        - output_dir (str): The directory to save the downloaded mp3 file.
    
    Returns:
        - str: The title of the YouTube video.
    """
    # Finding YouTube video
    yt = YouTube(url)
    logging.info(f'Attempting to download: {yt.title}')

    # Downloading best audio stream
    best_audio_stream = yt.streams.filter(progressive=False, type='audio').order_by('abr').desc().first()
    logging.info(f'Best audio stream: {best_audio_stream}')
    logging.info(f'Downloading to: {output_dir}')
    filepath = best_audio_stream.download(output_dir)
    logging.info(f'Downloaded')

    # Converting to mp3
    logging.info('Converting to mp3...')
    new_filepath = Path(filepath).with_name('audio').with_suffix('.mp3')
    subprocess.run(['ffmpeg', '-y', '-i', filepath, new_filepath])
    logging.info(f'Converted to: {new_filepath}')

    # Deleting original file
    logging.info('Deleting original file...')
    Path(filepath).unlink()
    logging.info('Deleted')

    logging.info('Download complete!')

    return yt.title

if __name__ == '__main__':
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    url = input('Enter YouTube video URL: ')
    output_dir = input('Enter output directory: ')
    download_youtube_video(url, output_dir)