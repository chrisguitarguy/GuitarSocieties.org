.PHONY: help init installpy installfe installrb dumpreq venv compilecss watchcss .gaurd 

help:
	@echo "Available Commands"
	@echo "------------------"
	@echo "  help - print this help"
	@echo ""
	@echo "  installpy - install the python dependencies"
	@echo "  installfe - install the frontend dependencies"
	@echo "  installrb - install the ruby tools required to build the CSS"
	@echo "  init - install the required libraries (python, ruby, & frontend)"
	@echo "  dumpreq - dump the python requirements to 'requirements.txt'"
	@echo "  venv - create a new virtual environment"
	@echo ""
	@echo "  compilecss - compile the SCSS files for the frontend"
	@echo "  watchcss - watch the SCSS files for changes, compiling when one is found"
	@echo ""

.guard:
	@if [ "${VIRTUAL_ENV}" == "" ]; then \
		echo "Please setup the Virtual Environment:"; \
		echo "  source .env/bin/activate"; \
		exit 1; \
	fi

.env:
	pyvenv .env

venv: .env

installpy: .gaurd
	pip install -r requirements.txt

installfe:
	bower install

installrb:
	bundle exec

init: installpy installfe installrb

dumpreq: .gaurd
	pip freeze > requirements.txt

compilecss:
	compass compile

watchcss:
	compass watch
