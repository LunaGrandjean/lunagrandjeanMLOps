# MLOps

## Pyenv

[Pyenv](https://github.com/pyenv/pyenv) allows developers of a given project to use the same Python version in an attempt of maintaining a reproducible environment including the Python version in an automated manner. You can obtain the latest version using this command. It is highly recommended to visit the project's homepage for more information.

```shell
curl https://pyenv.run | bash
```

Set the wanted python version and install it:
```shell
echo "3.11.6" > .python-version
pyenv install
```

Add the following lines to your ~/.bashrc or ~/.zshrc to initialize pyenv by default.

```shell
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

The command:
```bash
which python
```
Should return
```bash
~/.pyenv/shims/python
```

## Poetry

[Poetry](https://github.com/python-poetry/poetry) helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack everywhere.

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

Check if poetry is installed and with the correct version.

```shell
poetry --version
# If poetry is not recognized then you should investigate your $PATH variable.
export PATH="$PATH:$HOME/.poetry/bin"
```

Here an example of a `pyproject.toml` file
```toml
[tool.poetry]
name = "projet-name"
version = "0.1.0"
description = "Project description."
authors = ["Firstname Lastname <mail>"]

[tool.poetry.dependencies] # Direct prod dependencies
python = ">=3.11,<3.12"
streamlit = "~1"
pandas = "~2"

[tool.poetry.dev-dependencies] # Develop dependencies
coverage = "~7" # Allow to know the part of code covered
black = "~23" # Code formatting
isort = "~5" # Import sort
mypy = "~1" # Type checking
pytest = "~7" # For unit tests
vulture = "~2" # Check dead code
git-cliff = "~1" # Git commit formatting
```

Now to setup the project and install dependencies run these commands:
```bash
poetry config virtualenvs.prefer-active-python true # Use actual python env (here pyenv)
poetry config virtualenvs.in-project true # Generate dependencies in a .venv folder in the project
poetry install --no-root # Install dependencies (without the actual project)
```

You can add a dependencies by adding it in the file with the correct version and use the command `poetry update` or you can use the command `poetry add {LIB}` that will add it in the file with the correct version and install it.

## Makefile

Makefiles are commonly used in software development to automate the build process and ensure that the software is built consistently and efficiently. They can be used for a wide range of tasks, including compiling code, generating documentation, running tests, and deploying software.

Here an example of a `Makefile` for our use case:

```Makefile
prepare:
    poetry config virtualenvs.prefer-active-python true
    poetry config virtualenvs.in-project true
    poetry install --no-root
```
Just run `make prepare` and it will execute each listed commands

## Docker

To connect to the docker registry:
```shell
docker login -u "USERNAME" -p "PASSWORD" docker.io
```