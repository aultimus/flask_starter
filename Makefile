all:

save-deps:
	pip freeze > requirements.txt

install-deps:
	pip install -r requirements.txt

create-venv:
	python3 -m venv .venv

assume-venv:
	. .venv/bin/activate

create-db-file:
	touch file.db

run:
	DB_URL=sqlite:///$(PWD)/file.db flask --app flaskr run --debug

run-in-memory:
	DB_URL="sqlite:///:memory:" flask --app flaskr run --debug
