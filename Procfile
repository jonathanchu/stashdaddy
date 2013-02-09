web: newrelic-admin run-program; python manage.py compress; gunicorn stashdaddy.wsgi -b 0.0.0.0:$PORT
# celeryd: python manage.py celeryd -E -B --loglevel=INFO
