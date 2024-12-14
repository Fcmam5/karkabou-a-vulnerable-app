FROM python:latest

WORKDIR /

RUN pip install django django-rest-framework

EXPOSE 8000

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

RUN apt-get update && apt-get install -y build-essential
