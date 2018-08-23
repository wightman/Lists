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
from pymysql.err import IntegrityError



# UserList
# shows a list of all users, and lets you POST to add new users
class Users(Resource):
    @login_required
    def get(self):
#        response = {'status': 'sql error'}
#        responseCode = 500
        # parse query arguments: only one query-on allowed
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('userName', type=str, location='args')
        parser.add_argument('userEmail', type=str, location='args')
        parser.add_argument('userAdmin', type=bool, location='args')
        args = parser.parse_args()
        sqlProcName = 'getUsersAll'
        sqlProcArgs = ()
        if args['userAdmin'] is not None:
            sqlProcName = 'getUsersByAdmin'
            sqlProcArgs = (args['userAdmin'],)
        elif args['userName'] is not None:
            sqlProcName = 'getUsersByName'
            sqlProcArgs = (args['userName'],)
        elif args['userEmail'] is not None:
            sqlProcName = 'getUsersByEmail'
            sqlProcArgs = (args['userEmail'],)
        # open the sql connection and call the stored procedure
        db = pymysql.connect(settings.DBHOST,
            settings.DBUSER,
            settings.DBPASSWD,
            settings.DBDATABASE,
            charset='utf8mb4',
            cursorclass= pymysql.cursors.DictCursor
        )
        try:
            cursor = db.cursor()
            cursor.callproc(sqlProcName, sqlProcArgs)
            response = cursor.fetchall()
            responseCode = 200
        except Exception as e:
            response = {"status": e.args[1]}
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

    @admin_required
    def post(self):
        sqlProcName = 'addUser'
        # parse user data
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('userName', type = str,
            required=True, help='User name is required.')
        parser.add_argument('userEmail', type=str,
            required=True, help='User email address is required.')
        parser.add_argument('userPassword', type=str,
            required=True, help='User password is required.')
        parser.add_argument('userAdmin', type=bool)
        args = parser.parse_args()
        if args['userAdmin'] is None:
            args['userAdmin'] = False
        sqlProcArgs = [args['userName'], args['userEmail'], args['userPassword'], args['userAdmin'] ]

        # open the sql connection and call the stored procedure
        db = pymysql.connect(settings.DBHOST,
            settings.DBUSER,
            settings.DBPASSWD,
            settings.DBDATABASE,
            charset='utf8mb4',
            cursorclass= pymysql.cursors.DictCursor
        )
        try:
            cursor = db.cursor()
            cursor.callproc(sqlProcName, sqlProcArgs)
            db.commit()
            result = cursor.fetchone()
            uri = url_for('users', _external=True)
            uri = uri + '/' + str(result['LAST_INSERT_ID()'])
            response = { 'uri' : uri }
            responseCode = 201
        except IntegrityError as e:
            response = {"message": "Tsk. Tsk. Another user has that email address."}
            responseCode = 409
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

# End users.py
