# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response, url_for
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import dbSettings
from decorators import login_required, admin_required

import jsondate as json
from pymysql.err import IntegrityError

# Collaborators
# List owners, writers can post new items
class Items(Resource):
    @login_required
    def post(self, userId, listId):
        sqlProcName = 'getCollaborator'
        sqlProcArgs = (session['userId'], listId)
        # Can only request if the user is a collaborator - how to tell?
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
            if cursor.rowcount == 0:
                raise Exception("Not a collaborator for the list")
            response=cursor.fetchone()
            if response['accessType'] == 'R':
                raise Exception("No write access for the list")
        except Exception as e:
            response = {"message": e.args}
            responseCode = 403
            db.close()
            return make_response(jsonify(response), responseCode)
        sqlProcName = 'addItem'
        # parse user data
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('listId', type = int, location='json',
            required=True, help='A list ID is required.')
        parser.add_argument('itemName', type=str, location='json',
            required=True, help='An item name is required.')
        parser.add_argument('itemDetail', type=str, location='json',
            required=True, help='Item detail is required.')
        parser.add_argument('collaboratorId', type=str, location='json',
            required=True, help='Item collaboratorId is required.')
        args = parser.parse_args()
        sqlProcArgs = [args['listId'], args['itemName'], args['itemDetail'], args['collaboratorId'] ]
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
            result = cursor.fetchone()
            uri = url_for('items', userId = userId, listId = listId, _external=True)
            uri = uri + '/' + str(args['itemId'])
            response = { 'uri' : uri }
            responseCode = 201
        except Exception as e:
            response = {"message": e.args}
            responseCode = 500
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

    @login_required
    def get(self, userId, listId):
        sqlProcName = 'getCollaborator'
        sqlProcArgs = (session['userId'], listId)
        # Can only request if the user is a collaborator - how to tell?
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
            if cursor.rowcount == 0:
                raise Exception("Not a collaborator for the list")
        except Exception as e:
            response = {"message": e.args}
            responseCode = 403
            db.close()
            return make_response(jsonify(response), responseCode)
        sqlProcName = 'getItems'
        sqlProcArgs = (listId,)
        # Can only request if the user is a collaborator - how to tell?
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
            for piece in response:
               piece['uri']  = url_for('items', userId = userId, listId = listId,
                _external=True) + '/' + str(piece['itemId'])
            responseCode = 200
        except Exception as e:
            response = {"message": e.args}
            responseCode = 500
            db.close()
            return make_response(jsonify(response), responseCode)
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)


# End items.py
