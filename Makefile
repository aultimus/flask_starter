all: build

create-db-file:
	touch file.db

build:
	docker build . -t flask-starter

run:
	docker run --rm -it -p 5000:5000 --mount type=bind,src=./src/,dst=/src/ -e DB_URL="sqlite:////file.db" -e FLASK_DEBUG=true flask-starter:latest

run-in-memory:
	docker run --rm -it -p 5000:5000 --mount type=bind,src=./src/,dst=/src/ -e DB_URL="sqlite:///:memory:" -e FLASK_DEBUG=true flask-starter:latest

test:
	docker run --rm -it --mount type=bind,src=./src/,dst=/src/ flask-starter:latest poetry run pytest -s

run-local:
	DB_URL=sqlite:///$(PWD)/file.db poetry run flask --app flask-starter run --debug

run-local-in-memory:
	DB_URL="sqlite:///:memory:" poetry run flask --app flask-starter run --debug
