## ToSelf

run `git config --global core.autocrlf true` if on Windows or `git config --global core.autocrlf input` if on Mac/Linux

run `Set-ExecutionPolicy Unrestricted -Scope Process` if on Windows to give permissions to activate a venv

run `virtualenv --python=python3.11.6 .venv` to build a virtual environment and `activate.ps1` if on Windows or `activate` otherwise

run `pipenv install --dev` to install needed packages from pipfile/lock

run `pre-commit install` to install pre-commit hooks (black for PEP-8 formatting)

cd into `personal_assistant` folder and run `python -m main` to start the PA

run `deactivate` to exit the virtual env