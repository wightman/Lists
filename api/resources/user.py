# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response, url_for
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import dbSettings
from decorators import login_required, admin_required

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
        db = pymysql.connect(
            dbSettings.DB_HOST,
            dbSettings.DB_USER,
            dbSettings.DB_PASSWD,
            dbSettings.DB_DATABASE,
            charset='utf8mb4',
            cursorclass= pymysql.cursors.DictCursor
        )
        try:
            cursor = db.cursor()
            cursor.callproc(sqlProcName, sqlProcArgs)
            db.commit()
            response = cursor.fetchone()
            response['uri'] = url_for('users', _external=True) + '/' + str(response['userId'])
            responseCode = 200
        except Exception as e:
            response = {"status": e.args[1]}
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

    @login_required
    def put(self, userId):
        if userId != session['userId']:
            response = {'message': 'Owner privileges are required.'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)

        # Users can change their own info, except for userAdmin status.
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('userName', type=str, location='json',
            required=True, help='User name is required.')
        parser.add_argument('userEmail', type=str, location='json',
            required=True, help='User email address is required.')
        args = parser.parse_args()

        sqlProcName = 'putUser'
        sqlProcArgs = (userId, args['userName'], args['userEmail'])
        # open the sql connection and call the stored procedure
        db = pymysql.connect(
            dbSettings.DB_HOST,
            dbSettings.DB_USER,
            dbSettings.DB_PASSWD,
            dbSettings.DB_DATABASE,
            charset='utf8mb4',
            cursorclass= pymysql.cursors.DictCursor
        )
        try:
            cursor = db.cursor()
            cursor.callproc(sqlProcName, sqlProcArgs)
            db.commit()
            response = ''
            responseCode = 204
        except Exception as e:
            response = {"status": e.args[1]}
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

    @login_required
    def delete(self, userId):
        if userId != session['userId'] and session['userAdmin'] is not True:
            response = {'message': 'Owner or admin privileges are required.'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)

        sqlProcName = 'delUser'
        sqlProcArgs = (userId,)
        # open the sql connection and call the stored procedure
        db = pymysql.connect(
            dbSettings.DB_HOST,
            dbSettings.DB_USER,
            dbSettings.DB_PASSWD,
            dbSettings.DB_DATABASE,
            charset='utf8mb4',
            cursorclass= pymysql.cursors.DictCursor
        )
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

# End user.py
