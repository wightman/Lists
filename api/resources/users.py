# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response, url_for
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import settings
from decorators import login_required, admin_required

import jsondate as json
from urllib.parse import unquote
from struct import *



# UserList
# shows a list of all users, and lets you POST to add new users
class Users(Resource):
    @login_required
    def get(self):
        response = {'status': 'sql error'}
        responseCode = 500
        sqlProcName = 'getUsersAll'
        # open the sql connection and call the stored procedure
        db = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            cursor = db.cursor()
            cursor.callproc(sqlProcName, [])
            response = cursor.fetchall()
#            response = json.dumps(result)
            responseCode = 200
        except pymysql.MySQLError as e:
            return abort(404,message=unquote(e.args[1]) )
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

    @admin_required
    def post(self):
        sqlProcName = 'addUser'
        # parse user data
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name', required=True, help='required')
        parser.add_argument('email', required=True, help='required')
        parser.add_argument('passwd', required=True, help='required')
        parser.add_argument('admin', type=bool)
        args = parser.parse_args()
        passwd = args['passwd'].encode()
        if not 'admin' in args:
            args['admin'] = False
        sqlProcArgs = [args['name'], args['email'], passwd, args['admin'] ]

        response = {'status': 'sql error'}
        responseCode = 500
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
            result = cursor.fetchone()
            uri = url_for('users', _external=True)
            uri = uri + '/' + str(result['LAST_INSERT_ID()'])
            response = { 'uri' : uri }
            responseCode = 201
        except Exception as e:
            return abort(500,message=e )
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

# End.
