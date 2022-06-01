install: 
	# install commands
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	# format code with Black
lint:
	# pylint
test:
	#test
deploy:
	#deploy
all: install format lint test deploy