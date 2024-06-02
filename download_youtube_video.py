from pathlib import Path
from pytube import YouTube
from pydub import AudioSegment

def download_youtube_video(url, output_dir):

    # Finding YouTube video
    yt = YouTube(url)
    print('Attempting to download:', yt.title)

    # Downloading best audio stream
    audio_streams = yt.streams.filter(progressive=False, type='audio')
    best_audio_stream = yt.streams.filter(progressive=False, type='audio').order_by('abr').desc().first()
    print('\nBest audio stream:')
    print(best_audio_stream)
    print('\nDownloading...')
    filepath = best_audio_stream.download(output_dir)
    print('Downloaded to:', filepath)

    # Converting to mp3
    print('\nConverting to mp3...')
    audio = AudioSegment.from_file(filepath)
    new_filepath = Path(filepath).with_suffix('.mp3')
    audio.export(new_filepath, format='mp3')
    print('Converted to:', new_filepath)

    # Deleting original file
    print('\nDeleting original file...')
    Path(filepath).unlink()
    print('Deleted:', filepath)

    print('\nDone!')


if __name__ == '__main__':
    url = input('Enter YouTube video URL: ')
    output_dir = input('Enter output directory: ')
    download_youtube_video(url, output_dir)