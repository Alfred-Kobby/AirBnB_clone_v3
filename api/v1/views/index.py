#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:42:23 2023
@authors: Alfred Ternor
          Alex Sameri
"""
from flask import jsonify, Blueprint
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ check the status of route """
    return jsonify({'status': 'OK'})
