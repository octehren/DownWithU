import yt_dlp
import subprocess
from fastapi import HTTPException
from fastapi.responses import StreamingResponse

def stream_audio(url: str):
    try:
        # Options for yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',  # Download the best quality audio available
            'postprocessors': [{  # Convert to MP3
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '-',  # Stream to stdout instead of saving to a file
        }

        # Use yt-dlp to extract and stream the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info
            info_dict = ydl.extract_info(url, download=False)
            audio_url = info_dict['url']  # Get the direct audio stream URL

            # Use FFmpeg to convert and stream the audio
            ffmpeg_command = [
                'ffmpeg',
                '-i', audio_url,  # Input URL
                '-f', 'mp3',     # Output format
                '-'              # Stream to stdout
            ]

            # Start FFmpeg process
            process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Stream the output to the client
            return StreamingResponse(
                process.stdout,
                media_type="audio/mpeg",
                headers={
                    "Content-Disposition": f"attachment; filename={info_dict['title']}.mp3"
                }
            )

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error streaming audio: {str(e)}")