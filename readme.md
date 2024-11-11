# Simple YouTube Playlist MP3 Downloader

파이썬을 활용한 간단한 유튜브 플레이리스트 MP3 다운로더

## 운용환경

- Python 3.10 이상
- FFmpeg
- yt-dlp

## 설치 방법

1. FFmpeg 설치:
   - [FFmpeg 공식 웹사이트](https://ffmpeg.org/download.html)에서 다운로드
   - 시스템 환경 변수에 FFmpeg 경로 추가 또는 스크립트의 'ffmpeg_location' 경로 수정

2. 필요한 파이썬 패키지 설치:

~~~bash
pip install yt-dlp
~~~

## 사용 방법

1. 스크립트의 `playlist_url` 변수를 원하는 YouTube 플레이리스트 URL로 수정합니다.
2. 필요한 경우 다음 옵션들을 조정합니다:
   - `playliststart`: 다운로드 시작할 영상 번호
   - `playlistend`: 다운로드 종료할 영상 번호
   - `preferredquality`: MP3 품질 (기본값: 192kbps)
   - `output_path`: 다운로드 저장 경로 (기본값: 'downloads')

3. 스크립트 실행:

~~~bash
python youtube_to_mp3.py
~~~

## 주요 기능

- YouTube 플레이리스트의 영상들을 MP3 형식으로 변환
- 자동으로 다운로드 폴더 생성
- 재생목록 순서대로 파일명 지정
- 오류 발생 시 건너뛰고 계속 진행

## 설정 옵션 설명

~~~python
ydl_opts = {
    'format': 'bestaudio/best',           # 최상의 오디오 품질 선택
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',      # FFmpeg를 사용하여 오디오 추출
        'preferredcodec': 'mp3',          # MP3 형식으로 변환
        'preferredquality': '192',        # 192kbps 품질
    }],
    'outtmpl': '%(playlist_index)s-%(title)s.%(ext)s',  # 출력 파일 이름 형식
    'ffmpeg_location': r'C:\ffmpeg\bin',  # FFmpeg 설치 경로
    'playliststart': 1,                   # 시작할 영상 번호
    'playlistend': 117,                   # 마지막 영상 번호
    'ignoreerrors': True,                 # 오류 발생 시 계속 진행
}
~~~

## 문제 해결

1. FFmpeg 오류 발생 시:
   - FFmpeg가 올바르게 설치되어 있는지 확인
   - 'ffmpeg_location' 경로가 정확한지 확인

2. 다운로드 실패 시:
   - 인터넷 연결 상태 확인
   - YouTube 플레이리스트 URL이 유효한지 확인
   - 플레이리스트가 비공개가 아닌지 확인



