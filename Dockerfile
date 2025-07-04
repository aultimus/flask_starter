FROM python:3.13-slim

WORKDIR /app

# Install poetry for dependency management
ARG POETRY_VERSION=2.0.1
RUN pip install "poetry==${POETRY_VERSION}"

COPY src/ ./src/
COPY --chown=1000:1000 . .

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root

COPY ./src /src

ENV FLASK_APP="src/app.py"

EXPOSE 5000
# TODO: Use WSGI for Dockerfile and flask run in docker-compose.yml
# e.g. CMD ["gunicorn", "-b", "0.0.0.0:5000", "src.app:app"]
CMD ["poetry", "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]