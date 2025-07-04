all: build

install:
	poetry install

build:
	docker build . -t flask-starter

run:
	docker-compose up

unit-tests:
	pytest tests/unit-tests/

integration-tests:
	pytest tests/integration-tests/

system-tests:
	pytest tests/system-tests/
#	docker run --rm -it --mount type=bind,src=./src/,dst=/src/ flask-starter:latest poetry run pytest -s

test:
	$(MAKE) unit-tests
	$(MAKE) integration-tests
	$(MAKE) system-tests
