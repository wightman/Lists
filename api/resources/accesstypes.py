# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response, url_for
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import dbSettings
from decorators import login_required, admin_required

import jsondate as json
from pymysql.err import IntegrityError

class AccessTypes(Resource):
    # List collaborators can get collaboration information about members
    @login_required
    def get(self):
        sqlProcName = 'getAccessTypes'
        sqlProcArgs  = []
        db = pymysql.connect(
            dbSettings.DB_HOST,
            dbSettings.DB_USER,
            dbSettings.DB_PASSWD,
            dbSettings.DB_DATABASE,
            charset='utf8mb4',
            cursorclass= pymysql.cursors.DictCursor)
        try:
            cursor = db.cursor()
            cursor.callproc(sqlProcName, sqlProcArgs)
            response = cursor.fetchall()
            responseCode = 200
        except Exception as e:
            response = {"message": e.args}
            responseCode = 403
        db.close()
        return make_response(jsonify(response), responseCode)

# End accessTypes.py
