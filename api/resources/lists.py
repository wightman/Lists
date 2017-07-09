# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
import pymysql.cursors
import jsondate as json
from urllib.parse import unquote
from struct import *
import settings


# Lists
# - placeholder to allow use or url_for
#   in /users/<userId>/lists POST
class Lists(Resource):
    crap = True
