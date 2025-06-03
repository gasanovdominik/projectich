FROM python:3.12-slim

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y \
    gcc \
    netcat-openbsd \
    pkg-config \
    default-libmysqlclient-dev \
 && rm -rf /var/lib/apt/lists/*



RUN pip install --upgrade pip \
 && pip install -r requirements.txt


CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
