#!/bin/bash
if [ "$1" != "" ]; then
   /usr/local/bin/python /usr/src/app/web/manage.py pages make-message $1
fi

/usr/local/bin/gunicorn -c /usr/src/app/web/gunicorn.py app.wsgi:application &
sleep infinity 