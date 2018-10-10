# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response, url_for
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import dbSettings
from decorators import login_required, admin_required

import jsondate as json
from pymysql.err import IntegrityError

# Lists
# shows a list of all Lists, and lets you POST to add new Lists
class Lists(Resource):
    @login_required
    def get(self, userId):
        # must own the list to "ask" about it
        if userId != session['userId']:
            response = {'message': 'user lacks ownership'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)

        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('accessType', type=bool, location='args')
        args = parser.parse_args()
        sqlProcName = 'getLists'
        sqlProcArgs = ()
        if args['accessType'] is not None:
            sqlProcName = 'getUsersByAccess'
            sqlProcArgs = (request.args.get('accessType').upper(),)
        # open the sql connection and call the stored procedure
        db = pymysql.connect(
            dbSettings.DBH_OST,
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
            response = {"status": e.args[1]}
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

    @login_required
    def post(self, userId):
        if userId != session['userId']:
            response = {'message': 'cannot view lists of others'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)
        sqlProcName = 'addList'
        # parse user data
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('listName', type = str, location='json',
            required=True, help='List name is required.')
        parser.add_argument('listDescription', type=str, location='json',
            required=True, help='A desription of the list is required.')
        args = parser.parse_args()
        sqlProcArgs = [session['userId'], args['listName'], args['listDescription'] ]
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
            print(sqlProcArgs)
            cursor.callproc(sqlProcName, sqlProcArgs)
            print("cursor")
            db.commit()
            result = cursor.fetchone()
            print(result)
            uri = url_for('Lists', _external=True)
            uri = uri + '/' + str(result['@LastInsertId'])
            response = { 'uri' : uri }
            responseCode = 201
        except IntegrityError as e:
            response = {"message": "WAT?. You already have that list by that name."}
            responseCode = 409
        except Error as e:
            response = {"message": ""}
            responseCode = 500
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

# End Lists.py
