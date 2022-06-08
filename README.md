[![Python application test with Github Actions](https://github.com/bilal-khan-dev/python-wiki-microservice/actions/workflows/devops.yml/badge.svg)](https://github.com/bilal-khan-dev/python-wiki-microservice/actions/workflows/devops.yml)

# python-wiki-microservice

## Project Scaffold

1. Create a Python Virtual Enviroment `python3 -m venv ~/.venv` or `virtualenv ~/.venv`.
2. Create empty files `Makefile`, `requirement.txt`, `main.py`, `Dockerfile`, `mylib/__init__.py`.
3. Populate `Makefile`.
4. Setup Continuous Integeration.
5. Adding linting with `make lint`, testing feature with `make test` and formatting with `make format`.
6. Testing logic by building a cli using Python Fire Library `./cli-fire.py --help`.
7. Containerize the microservice with docker `docker build .`
