#!/bin/bash
/etc/init.d/nginx restart
/usr/local/bin/python /usr/src/app/web/manage.py collectstatic --noinput 
/usr/local/bin/gunicorn -c /usr/src/app/web/gunicorn.py app.wsgi:application &
sleep infinity 