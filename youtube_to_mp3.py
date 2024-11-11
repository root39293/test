import yt_dlp
import os

def download_playlist(output_path='downloads'):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        # yt-dlp 옵션 설정
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(playlist_index)s-%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': True,
            'ffmpeg_location': r'C:\ffmpeg\bin',
            'playliststart': 1,
            'playlistend': 117,
            'ignoreerrors': True,
            'extract_flat': False,
            'playlist_items': '1-117'
        }
        
        print(f"재생목록 다운로드 시작...")
        
        playlist_url = "https://www.youtube.com/watch?v=Fvc9ujWvFIY&list=PL_qjC9d3KiXJ1scKLBQtdY9Lq9cM2atgA"
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
            
        print(f"재생목록 다운로드 완료!")
        
    except Exception as e:
        print(f"에러 발생: {str(e)}")

if __name__ == "__main__":
    download_playlist() 