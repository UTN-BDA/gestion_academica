#!/bin/bash

echo "Make migrations"
python manage.py makemigrations app
echo "-----------------------------------------------"

echo "Applying migrations"
python manage.py migrate
echo "-----------------------------------------------"

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
echo "-----------------------------------------------"