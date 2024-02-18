# minstrel

An instrumentation hardware orchestration platform.

## Install

### PyPI

Install and update using pip:

```shell
pip install -U minstrel
```

### Repository

When using git, clone the repository and change your 
present working directory.

```shell
git clone http://github.com/mcpcpc/minstrel
cd minstrel/
```

Create and activate a virtual environment.

```shell
python -m venv venv
source venv/bin/activate
```

Install minstrel to the virtual environment.

```shell
pip install -e .
```

## Commands

### db-init

The backend database can be initialized or re-initialized 
with the following command.

```shell
quart --app minstrel init-db
```

### token

In order to prevent unauthorized or accidental backend
database manipulation, some API actions require a *token*
key argument. Token strings can be generated with the
following command.

```shell
quart --app minstrel token
```

The token command also accepts an integer argument that
defines the duration (in seconds) in which the generated
token is valid. The default argument value is `300`.

Note that changing the `SECRET_KEY` variable will
invalidate any previously generated tokens once the
application instance is restarted. 

## Docker Container

Pulling the latest container image from command line.

```shell
docker pull ghcr.io/mcpcpc/minstrel:latest
```

## Deployment

Before deployment, overriding the default `SECRET_KEY`
variable is *strongly* encourage. This can be done by
creating a `conf.py` file and placing it in the
same root as the instance (i.e. typically where the
backend database resides).

```python
SECRET_KEY = “192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf“
```

There are a number of ways to generate a secret key
value. The simplest would be to use the built-in secrets
Python library.

```shell
$ python -c ‘import secrets; print(secrets.token_hex())’
‘192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf’
```

### Quart

Non-production ASGI via quart for development and
debugging.

```shell
quart --debug --app minstrel run
```

### Uvicorn

Production ASGI via uvicorn.

```shell
pip install uvicorn
uvicorn --factory minstrel:create_app
```

## Test

```shell
python3 -m unittest
```

Run with coverage report.

```shell
coverage run -m unittest
coverage report
coverage html  # open htmlcov/index.html in a browser
```
