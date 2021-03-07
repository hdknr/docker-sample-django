from django.utils import timezone as tz
from django.http import HttpResponse
import os
import json
from django.conf import settings
from . import utils
from logging import getLogger

logger = getLogger()


def index(request, path):
    now = tz.now()
    name = "message.json"

    if utils.fixture_exists(name):
        fixture = json.load(utils.open_fixture(name))
    else:
        fixture = {}

    params = {
        "path": path,
        "now": str(now),
        "ver": settings.APP_VER,
        **os.environ,
        **fixture,
    }
    text = json.dumps(params, ensure_ascii=False, indent=2)
    logger.info(text)
    return HttpResponse(text, content_type="application/json")
