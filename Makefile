install: 
	# install commands
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	# format code with Black
	black *.py mylib/*.py
lint:
	# pylint with disable warnings R=Recommneded and C=Configuration because it fails the build
	# Its too much verbose for a build process
	pylint --disable=R,C *.py mylib/*.py
test:
	# By default, pytest will not show test durations that are too small (<0.005s) unless -vv flag is passed.
	python3 -m pytest -vv --cov=mylib --cov=main test_*.py 
build:
	#build container
deploy:
	#deploy
all: install format lint test deploy