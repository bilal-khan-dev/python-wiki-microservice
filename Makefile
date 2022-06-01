install: 
	# install commands
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	# format code with Black
	black *.py mylib/*.py
lint:
	# pylint
test:
	#test
deploy:
	#deploy
all: install format lint test deploy