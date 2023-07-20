FROM python:3.9

WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD . /app/

CMD ["gunicorn", "-b", ":8000", "djangoProject.wsgi"]
