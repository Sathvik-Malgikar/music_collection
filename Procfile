release: python manage.py migrate
release: python manage.py loaddata data.json
web: gunicorn music_collection.wsgi --log-file -