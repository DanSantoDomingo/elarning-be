#!/bin/bash

# Apply database migrations
echo "start django migrations"

python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the server
echo "start django"
# gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 2
python manage.py runserver 0.0.0.0:8000 --nostatic
# gunicorn backend.wsgi:application --bind 0.0.0.0:8000