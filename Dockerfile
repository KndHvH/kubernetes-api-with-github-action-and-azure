FROM python:3.10 as base

WORKDIR /app


EXPOSE 8000

COPY Pipfile .
RUN pip install pipenv

FROM base AS dependencies
RUN pipenv install --system --skip-lock

FROM base AS development
RUN pipenv install --system --dev --skip-lock
COPY . .

FROM dependencies AS production
COPY app app
COPY run.py .