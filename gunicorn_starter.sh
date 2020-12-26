#!/bin/sh
gunicorn --chdir /usr/src/app appserver:app -w 2 --threads 2 -b 0.0.0.0:8000