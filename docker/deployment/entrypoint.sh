if [ -L /etc/nginx/sites-enabled/default ]; then
   unlink /etc/nginx/sites-enabled/default
fi
service ssh restart
service nginx start
/usr/local/bin/gunicorn -c /usr/src/app/web/gunicorn.py app.wsgi:application
# exec "$@"