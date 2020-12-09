FROM python:3-alpine

ARG ENCODED_PROXY
ARG HTTP_PROXY=http://$ENCODED_PROXY
ARG HTTPS_PROXY=http://$ENCODED_PROXY

WORKDIR /usr/src
COPY . ./app
WORKDIR /usr/src/app

EXPOSE 8000
RUN apt-get install libpq-dev
RUN pip install -qr requirements.txt

#CMD ["python3", "manage.py db upgrade"]
#CMD ["python3", "appserver.py"]
RUN /bin/sh -c "python3 manage.py db upgrade"
#RUN /bin/sh -c "python3 ./appserver.py"
CMD ["python3", "appserver.py"]