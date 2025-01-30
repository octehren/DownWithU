# DownWithU
Youtube downloader. Uses both pytube and youtube-dl.

## Running the Back-End
```bash
# Optional but highly recommended: set-up pyenv version. See: https://dev.to/otamm/python-version-management-with-pyenv-3fig
pyenv local 3.12
# Optional but highly recommended: setup virtual env
python -m venv .venv && source .venv/bin/activate
# installs packages to venv context
python -m pip install fastapi uvicorn pytube youtube-dl
```