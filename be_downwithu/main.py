from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import FileResponse
import yt_dlp
import os

app = FastAPI()

def download_audio(url: str, output_dir: str = "downloads") -> str:
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Options for yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',  # Download the best quality audio
            'postprocessors': [{  # Convert to MP3
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{output_dir}/%(title)s.%(ext)s',  # Output file template
            'noplaylist': True,  # Download only the single video, not the playlist
        }

        # Download the audio and get the file path
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)  # Extract video info
            file_path = ydl.prepare_filename(info_dict)  # Get the downloaded file path
            return file_path.replace(".webm", ".mp3")  # Replace extension for MP3

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error downloading audio: {str(e)}")

@app.get("/download_audio/")
async def download_youtube_audio(url: str = Query(..., description="The YouTube video URL")):
    # Download the audio file
    audio_file_path = download_audio(url)

    # Return the file as a response
    return FileResponse(audio_file_path, media_type="audio/mpeg", filename=os.path.basename(audio_file_path))

# Run the app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)