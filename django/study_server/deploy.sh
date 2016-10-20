#!/bin/bash
kill -9 $(sudo lsof -t -i:8000)
cp ./study_server/wsgi.py ./
gunicorn wsgi --workers=3 --bind  0.0.0.0:8000 
