# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import settings
from decorators import admin_required

from pymysql.err import IntegrityError

#
# Allows an admin to alter admin status for *another* user
#
class Admin(Resource):
    @admin_required
    def put(self, userId):
        if userId == session['userId']:
            response = {'message': 'Admin cannot dimish their own privileges.'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)

        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('userAdmin', type=bool, location='args')
        args = parser.parse_args()
        if args['userAdmin'] == 1:
            session['userAdmin'] = True
        else:
            session['userAdmin'] = False

        sqlProcName = 'putUserAdmin'
        sqlProcArgs = (userId, session['userAdmin'],)

        # open the sql connection and call the stored procedure
        db = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            cursor = db.cursor()
            cursor.callproc(sqlProcName, sqlProcArgs)
            db.commit()
            responseCode = 204
        except Exception as e:
            abort(404, e.args[1])
        finally:
            #close dbConnection
            db.close()
            return 204


# End admin.py
