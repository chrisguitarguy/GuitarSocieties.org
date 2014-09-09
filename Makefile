.PHONY: help init dumpreq venv .gaurd 

help:
	@echo "Available Commands"
	@echo "------------------"
	@echo "  help - print this help"
	@echo ""
	@echo "  init - install the required libraries"
	@echo "  dumpreq - dump the requirements to 'requirements.txt'"
	@echo "  venv - create a new virtual environment"

.guard:
	@if [ "${VIRTUAL_ENV}" == "" ]; then \
		echo "Please setup the Virtual Environment:"; \
		echo "  source .env/bin/activate"; \
		exit 1; \
	fi

.env:
	pyvenv .env

venv: .env

init: .guard
	pip install -r requirements.txt

dumpreq: .gaurd
	pip freeze > requirements.txt
