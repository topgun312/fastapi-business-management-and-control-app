FROM python:3.10


RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY pyproject.toml .

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/fastapi_app

RUN chmod a+x docker/*.sh



