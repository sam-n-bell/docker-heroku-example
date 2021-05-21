FROM python:3.7.9
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000

CMD ["python" ,"app.py"]