# yt-playlist-dl

A simple tool for converting YouTube playlists to MP3 format

## Requirements
- Python 3.10+
- FFmpeg
- yt-dlp (`pip install yt-dlp`)

## Usage

1. Install FFmpeg and set environment variables
2. Set YouTube playlist URL in playlist_url variable
3. Run: `python youtube_to_mp3.py`

## Main Settings
~~~python
ydl_opts = {
   'format': 'bestaudio/best',
   'postprocessors': [{
       'key': 'FFmpegExtractAudio',
       'preferredcodec': 'mp3',
       'preferredquality': '192'
   }],
   'playliststart': 1,    # Start video
   'playlistend': 117,    # End video
   'ignoreerrors': True   # Ignore errors
}
~~~
