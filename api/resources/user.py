# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import settings
from decorators import login_required, admin_required, privilege_required, owner_required

import jsondate as json
from urllib.parse import unquote
from pymysql.err import IntegrityError

# Todo
# shows a single user and lets you delete a user
class User(Resource):
    @login_required
    def get(self, userId):
        print('getUser')
        sqlProcName = 'getUser'
        sqlProcArgs = (userId,)
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
            response = cursor.fetchall()
            if response:
                responseCode = 200
            else:
                response = {"status": "Resource not found."}
                responseCode = 404
        except Exception as e:
            response = {"status": e.args[1]}
            responseCode = 500
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

    @privilege_required
    def delete(self, userId):
        sqlProcName = 'delUser'
        sqlProcArgs = (userId,)
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
            response = cursor.fetchall()
            responseCode = 204
        except Exception as e:
            response = {"status": e.args[1]}
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
            return responseCode

    @owner_required
    def put(self, userId):
        # Users can change their own info, except for userAdmin status.
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('userName', type=str, location='json',
            required=True, help='User name is required.')
        parser.add_argument('userEmail', type=str, location='json',
            required=True, help='User email address is required.')
        args = parser.parse_args()

        #
        #
        print('parsed args')
        print(args)
        sqlProcName = 'putUser'
        sqlProcArgs = (userId, args['userName'], args['userEmail'])
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
            return abort(404,message=unquote(e.args[1]) )
        finally:
            #close dbConnection
            db.close()
            return responseCode

# End user.py
