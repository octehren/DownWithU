from fastapi.testclient import TestClient
from app.main import app

from tests.helpers import get_random_invalid_video_url, get_random_valid_video_url

client = TestClient(app)

def test_download_audio_success():
    # Test successful API request
    response = client.get(f"/download_audio?url={get_random_valid_video_url()}")
    assert response.status_code == 200
    assert response.headers["content-type"] == "audio/mpeg" # if response is audio, assume everything is working

def test_download_audio_failure():
    # Test failure case (invalid URL)
    response = client.get(f"/download_audio?url={get_random_invalid_video_url()}")
    assert response.status_code == 400
    assert "Error streaming audio" in response.json()["detail"] # jack-of-all-trades failure