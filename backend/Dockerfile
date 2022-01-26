FROM python:3.8-slim as base

FROM base as builder

RUN mkdir /setup
WORKDIR /setup

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --prefix=/setup -r requirements.txt

# Build run image.
FROM base

WORKDIR /app

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY --from=builder /setup /usr/local

COPY . .

EXPOSE 8000

CMD [ "sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]