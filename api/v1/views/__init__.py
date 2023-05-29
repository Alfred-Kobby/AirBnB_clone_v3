#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:42:23 2023
@authors: Alfred Ternor
          Alex Sameri
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


if (__name__ == 'api.v1.views'):
    from api.v1.views.index import *

