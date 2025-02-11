all:

save-deps:
	pip freeze > requirements.txt

install-deps:
	pip install -r requirements.txt

create-venv:
	python3 -m venv .venv

assume-venv:
	. .venv/bin/activate

run:
	DB_URL="sqlite:///:memory:" flask --app flaskr run --debug