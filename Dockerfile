FROM ubuntu:latest
RUN apt-get -y update && apt-get install -y apt-utils && apt-get -y install python3 && apt-get -y install python3-pip
RUN pip3 install --upgrade pip
WORKDIR /app
COPY app /app
RUN pip install -r requirements.txt
RUN adduser roeeyn
USER roeeyn
EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:5000 wsgi
#CMD gunicorn --bind 0.0.0.0:$PORT wsgi
