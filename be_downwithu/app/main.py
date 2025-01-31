from fastapi import FastAPI, Query
from app.services.stream_audio_service import stream_audio

app = FastAPI()

@app.get("/download_audio")
async def download_youtube_audio(url: str = Query(..., description="The YouTube video URL")):
    return stream_audio(url)

# Run the app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)