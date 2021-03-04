from django.apps import apps
from pathlib import Path


def get_fixture(name):
    conf = apps.get_app_config("pages")
    return Path(conf.path, f"fixtures/{name}")


def fixture_exists(name):
    return get_fixture(name).is_file()


def open_fixture(name, *args, **kwargs):
    return get_fixture(name).open(*args, **kwargs)
