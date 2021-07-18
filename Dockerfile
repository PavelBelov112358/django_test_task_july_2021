FROM python:3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt --no-cache-dir

COPY . /app/
