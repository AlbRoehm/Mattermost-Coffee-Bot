# Use the official Python 3.12 image
FROM python:3.12

# Set the working directory

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /.

COPY pyproject.toml poetry.lock ./
RUN touch README.md
RUN poetry install #--without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY . .

RUN poetry install #--without dev

COPY ./.venv/lib/python3.12/site-packages/mattermostdriver/websocket.py ./.venv/lib/python3.12/site-packages/mattermostdriver/websocket.py

# Run the application
CMD ["poetry", "run", "python", "-u", "-m", "main"]
