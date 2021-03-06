#!/bin/bash
if [ -L /etc/nginx/sites-enabled/default ]; then
   unlink /etc/nginx/sites-enabled/default
fi
service ssh restart
service nginx start
if [ "$1" != "" ]; then
   /usr/local/bin/python /usr/src/app/web/manage.py pages make-message $1
fi
/usr/local/bin/gunicorn -c /usr/src/app/web/gunicorn.py app.wsgi:application
# exec "$@"