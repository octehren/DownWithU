from pytest import fixture, raises
from pytest_mock import MockerFixture

from fastapi import HTTPException
from fastapi.responses import StreamingResponse

from app.services.stream_audio_service import stream_audio
from tests.helpers import get_random_invalid_video_url, get_random_valid_video_url


@fixture
def mocks(mocker: MockerFixture):
    # Mock the YDL class
    mock_ydl_instance = mocker.MagicMock()
    # Provide default return_value
    mock_ydl_instance.extract_info.return_value = {"url": "mock_url", "title": "mock_title"}
    mocker.patch("yt_dlp.YoutubeDL", return_value=mock_ydl_instance)

    # Mock subprocess.Popen
    mock_process = mocker.MagicMock()
    mock_process.stdout = b"mock_audio_data"
    mocker.patch("subprocess.Popen", return_value=mock_process)

    # Return the two mock objects
    return mock_ydl_instance, mock_process


def test_stream_audio_success(mocks):
    response = stream_audio(get_random_valid_video_url())

    assert isinstance(response, StreamingResponse)
    assert response.media_type == "audio/mpeg"


def test_stream_audio_failure(mocks, mocker: MockerFixture):
    # Make the subprocess raise an exception
    mocker.patch("subprocess.Popen", side_effect=Exception("Mock error"))

    # Exception should rise within this block
    with raises(HTTPException) as exc_info:
        stream_audio(get_random_invalid_video_url())

    assert exc_info.value.status_code == 400
    assert "Error streaming audio:" in exc_info.value.detail