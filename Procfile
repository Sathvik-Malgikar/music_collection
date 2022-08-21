release: python manage.py loaddata data.json
         python manage.py migrate
web: gunicorn music_collection.wsgi --log-file -