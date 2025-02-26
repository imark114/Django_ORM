FROM python:3.12.8-alpine3.20

ENV PYTHONBUFFERED=1

WORKDIR /django_ecommerce

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000

EXPOSE 8000