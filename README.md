# DownWithU
Youtube downloader. Uses both pytube and youtube-dl.

## Example uses (Back-End)
**Note**: These examples assume the Back-end is running locally on port `8000`. The pieces of content used as examples are all copyright-free material.

- Example 1 ("Chollima on the Wing"): `http://127.0.0.1:8000/download_audio/?url=https://www.youtube.com/watch?v=DKsj5mCR7qs`
- Example 2 ("I Love Beijing Tiananmen"): `http://127.0.0.1:8000/download_audio/?url=https://www.youtube.com/watch?v=mJmjljQP3oY`
- Example 3, shortest one (Linux Startup Sound): `http://127.0.0.1:8000/download_audio/?url=https://www.youtube.com/watch?v=rnbX7VUvxGU`

## Back-End Setup
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