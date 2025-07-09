# Use official Python image
FROM python:3.11-slim

# Install poetry
RUN pip install poetry

# Create workdir
WORKDIR /app

# Copy only relevant files
COPY README.md pyproject.toml poetry.lock ./

# Install deps without virtualenv (Poetry v1.2+)
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Copy rest of code
COPY . .
