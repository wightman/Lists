# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import dbSettings
from decorators import login_required

from pymysql.err import IntegrityError

#
# Allows a user to change their password
#
class Password(Resource):
    @login_required
    def put(self):
        userId = session['userId']
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('userPassword', type=str, location='json',
            required=True, help='User\'s current password is required.')
        parser.add_argument('newPassword', type=str, location='json',
            required=True, help='User\'s new password is required.')
        args = parser.parse_args()

        sqlProcName = 'putUserPassword'
        sqlProcArgs = (userId, args['userPassword'], args['newPassword'])
        print(sqlProcArgs)
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
# End password.py
