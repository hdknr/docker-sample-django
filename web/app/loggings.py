import os
import sys


def default_base():
    base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(base, "logs")


def get_logfile(name):
    base = os.environ.get("DJ_LOGDIR", default_base())
    if not os.path.isdir(base):
        os.makedirs(base)
    return os.path.join(base, name)


def handler_file(name, level="DEBUG"):
    return {
        # 'level': level,
        "class": "logging.FileHandler",
        "filename": get_logfile(name),
        "formatter": "verbose",
    }


FORMATTERS = {
    "verbose": {
        "format": "\n{levelname} {asctime} {module} {process} {thread} \n{filename} {funcName} {lineno} {message}\n",
        "style": "{",
    },
}

HANDLERS_CONSOLE = {
    "level": "INFO",
    "class": "logging.StreamHandler",
    "stream": sys.stdout,
    "formatter": "verbose",
}

LOGGING_OLD = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": FORMATTERS,
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    },
    "handlers": {
        "file": handler_file("app.log", level="DEBUG"),
        "console": HANDLERS_CONSOLE,
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        }
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}