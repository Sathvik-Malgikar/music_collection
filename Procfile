release: python manage.py loaddata data.json
         python manage.py migrate
         python manage.py collectstatic
web: gunicorn music_collection.wsgi --log-file -