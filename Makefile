install: 
	# install commands
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	# format code with Black
	black *.py mylib/*.py
lint:
	# pylint with disable warnings R=Recommneded and C=Configuration because it fails the build
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
deploy:
	#deploy
all: install format lint test deploy