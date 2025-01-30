# DownWithU
Youtube downloader. Uses both pytube and youtube-dl.

## Running the Back-End
```bash
# Optional but highly recommended: set-up pyenv version. See: https://dev.to/otamm/python-version-management-with-pyenv-3fig
pyenv local 3.12
# Optional but highly recommended: setup virtual env
python -m venv .venv && source .venv/bin/activate
# Optional: setup direnv. See: https://dev.to/otamm/one-environment-per-project-manage-directory-scoped-envs-with-direnv-in-posix-systems-4n3c
touch .envrc && echo 'export VIRTUAL_ENV=."venv" && layout python' >> .envrc && direnv allow
# installs packages to venv context
python -m pip install fastapi uvicorn pytube youtube-dl
# writes libraries and versions to a reusable file
pip freeze > requirements.txt 
```