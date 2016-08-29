#!/bin/bash
kill -9 $(sudo lsof -t -i:20000)
cp ./study_server/wsgi.py ./
gunicorn wsgi --bind 0.0.0.0:20000
