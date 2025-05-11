#!/bin/bash

echo "Make migrations"
python /app/manage.py makemigrations
echo "-----------------------------------------------"

echo "Applying migrations"
python /app/manage.py migrate
echo "-----------------------------------------------"

echo "Starting server"
python /app/manage.py runserver 0.0.0.0:8000
echo "-----------------------------------------------"