# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import dbSettings
from decorators import admin_required

from pymysql.err import IntegrityError

#
# Allows an admin to alter admin status for *another* user
#
class Admin(Resource):
    @admin_required
    def put(self, userId):
        if userId == session['userId']:
            response = {'message': 'Admin cannot alter their own privileges.'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)

        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('userAdmin', type=bool, location='json',
            required=True, help='new boolean userAdmin status required.')
        args = parser.parse_args()

        sqlProcName = 'putUserAdmin'
        sqlProcArgs = (userId, args['userAdmin'],)
        # open the sql connection and call the stored procedure
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
            db.commit()
            response = ''
            responseCode = 204
        except Exception as e:
            response = jsonify({"status": e.args[1]})
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
        return make_response(response, responseCode)


# End admin.py
