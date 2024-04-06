run:
	./venv/bin/python -m bot

venv:
	python -m venv venv
	./venv/bin/pip install -r requirements.txt
