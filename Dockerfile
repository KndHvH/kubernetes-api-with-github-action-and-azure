FROM python:3.10

COPY . .

RUN pip install pipenv
RUN pipenv install

EXPOSE 8000

CMD ["pipenv","run","uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]