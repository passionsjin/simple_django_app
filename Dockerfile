FROM python:3.7.3
ENV PYTHONUNBUFFERED 1
RUN git clone https://github.com/passionsjin/simple_django_app.git

WORKDIR /simple_django_app/simpleapp

RUN pip install -r requirements.txt

RUN python manage.py migrate

