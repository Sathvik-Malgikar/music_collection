release: python manage.py loaddata data.json
release: python manage.py migrate
web: gunicorn music_collection.wsgi --log-file -