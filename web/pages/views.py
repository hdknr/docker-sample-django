from django.shortcuts import render
from django.utils import timezone as tz
from django.http import HttpResponse
import os
from django.conf import settings
from logging import getLogger
logger = getLogger()

def index(request, path):
    now = tz.now()
    db_params = os.environ.get('DATABASE_PARAMS', {})
    text  = f'Super Cool Pages {now} : {path} :{db_params} : Ver={settings.APP_VER}'
    logger.info(text)
    return HttpResponse(text)