all:

save-deps:
	pip freeze > requirements.txt

create-venv:
	python3 -m venv .venv

assume-venv:
	. .venv/bin/activate

run:
	flask --app flaskr run --debug