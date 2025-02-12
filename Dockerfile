FROM python:3.13-slim

# Install poetry for dependency management
ARG POETRY_VERSION=2.0.1
RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root

COPY ./flaskr /flaskr

ENV FLASK_APP="/flaskr/__init__.py"

EXPOSE 5000
CMD ["poetry", "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]