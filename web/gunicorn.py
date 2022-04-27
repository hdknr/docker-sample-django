"""
gunicorn -c gunicorn.py  app.wsgi:application
"""
import sys

import environ
import gunicorn

BASE_DIR = environ.Path(__file__) - 1
PROJECT_DIR = BASE_DIR - 1  #
ENV = environ.Env()
ENV.read_env(env_file=str(PROJECT_DIR.path(".env")))


# for Gunicorn to find app.wsgi:application
sys.path.append(str(BASE_DIR))

# logs
# http://gunicorn-docs.readthedocs.org/en/latest/deploy.html#logging
#
#  kill -USR1 $(cat /var/run/gunicorn.pid)
#

# Gunicorn Configuration
gunicorn.SERVER_SOFTWARE = ENV("GUNICORN_PROCESS", default="Gunicorn")
timeout = ENV.int("GUNICORN_TIMEOUT", default=180)
bind = ENV.str("GUNICORN_BIND", default=f"unix:{PROJECT_DIR}/logs/gunicorn.sock")
pidfile = ENV.str("GUNICORN_PIDFILE", default=f"{PROJECT_DIR}/logs/gunicorn.pid")
accesslog = ENV.str("GUNICORN_ACCESSLOG", default="-") or "-"
errorlog = ENV.str("GUNICORN_ERRORLOG", default="-") or "-"
