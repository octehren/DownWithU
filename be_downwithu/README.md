# DownWithU Back-End
Youtube downloader. Uses yt-dlp.

## Quickstart

Run with docker:

```bash
docker build -t downwithu . && docker run -p 8000:8000 downwithu
```

If you need to inspect the container:
```bash
docker exec -it downwithu /bin/sh
```

## Example uses (Back-End)
**Note**: These examples assume the Back-end is running locally on port `8000`. The pieces of content used as examples are all copyright-free material.

- Example 1 ("Chollima on the Wing"): `http://127.0.0.1:8000/download_audio?url=https://www.youtube.com/watch?v=DKsj5mCR7qs`
- Example 2 ("I Love Beijing Tiananmen"): `http://127.0.0.1:8000/download_audio?url=https://www.youtube.com/watch?v=mJmjljQP3oY`
- Example 3, shortest one (Linux Startup Sound): `http://127.0.0.1:8000/download_audio?url=https://www.youtube.com/watch?v=rnbX7VUvxGU`

## Back-End Setup

First, install `ffmpeg`.
```bash
sudo apt-get install ffmpeg # debian-based Linux distros
brew install ffmpeg # macOS
# For windows, see: https://ffmpeg.org/download.html
```

```bash
# Optional but highly recommended: set-up pyenv version. See: https://dev.to/otamm/python-version-management-with-pyenv-3fig
pyenv local 3.12
# Optional but highly recommended: setup virtual env
python -m venv .venv && source .venv/bin/activate
# Optional: setup direnv. See: https://dev.to/otamm/one-environment-per-project-manage-directory-scoped-envs-with-direnv-in-posix-systems-4n3c
touch .envrc && echo 'export VIRTUAL_ENV=."venv" && layout python' >> .envrc && direnv allow
# installs packages to venv context
python -m pip install "fastapi[standard]" yt-dlp
# writes libraries and versions to a reusable file
pip freeze > requirements.txt 
```

## Running App

Use this commands from the same directory level as `pyproject.toml`:

```bash
fastapi run # prod mode
fastapi run --reload # dev mode
```

## Updating

Sometimes Youtube might update the website and make this package's functionality break.
To update the main dependency that enables the download, run:

```bash
bash self_update.sh
```

This will update `yt-dlp` and then overwrite `requirements.txt` with the new version.
This should probably be put into a cron job or something to guarantee an always up to date service.

**NOTE**: it won't automatically self-update as of no

## Testing

If you wish to test locally:

```bash
python -m pip install -r requirements_test.txt
pytest test/
```

Run only integration tests (these are the most important as they check the core library's current working status):

```bash
pytest tests/integration
```

Testing the self-updater script:

```bash
bash test_self_update.sh
```