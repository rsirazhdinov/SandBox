FROM python:3-alpine

ARG ENCODED_PROXY
ARG HTTP_PROXY=http://$ENCODED_PROXY
ARG HTTPS_PROXY=http://$ENCODED_PROXY

ARG SANDBOX_DB_SANDBOX_DB_PG_SERVICE_PORT
WORKDIR /usr/src
COPY . ./app
WORKDIR /usr/src/app



EXPOSE 8000
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -qr requirements.txt

#CMD ["python3", "manage.py db upgrade"]
#CMD ["python3", "appserver.py"]
#RUN /bin/sh -c "python3 manage.py db downgrade"
#RUN /bin/sh -c "python3 manage.py db downgrade"

#RUN /bin/sh -c "python3 manage.py db upgrade"
#RUN /bin/sh -c "gunicorn --chdir /usr/src/app appserver:app -w 2 --threads 2 -b 0.0.0.0:8000"
#RUN /bin/sh -c "python3 ./appserver.py"
#CMD ["python3", "appserver.py"]
ENTRYPOINT ["./gunicorn_starter.sh"]

