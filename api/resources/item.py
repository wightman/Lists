# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response, url_for
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import dbSettings
from decorators import login_required, admin_required

import jsondate as json
from pymysql.err import IntegrityError

class Item(Resource):
    # List collaborators can get list items
    @login_required
    def get(self, userId, listId, itemId):
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
        sqlProcName = 'getItem'
        sqlProcArgs = (itemId, )
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
            response = cursor.fetchone()
            response['uri']  = url_for('items', userId = userId, listId = listId,
                _external=True) + '/' + str(response['itemId'])
            responseCode = 200
        except Exception as e:
            response = {"message": e.args}
            responseCode = 500
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

    @login_required
    def put(self, userId, listId, itemId):
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
        sqlProcName = 'putItem'
        # parse user data
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('itemName', type=str, location='json',
            required=True, help='An item name is required.')
        parser.add_argument('itemDetail', type=str, location='json',
            required=True, help='Item detail is required.')
        parser.add_argument('completed', type=bool, location='json',
            required=True, help='Item completion status is required.')
        parser.add_argument('itemPosition', type=int, location='json',
            required=True, help='itemPosition is required.')
        args = parser.parse_args()
        sqlProcArgs = [itemId, args['itemName'], args['itemDetail'],
            args['itemPosition'], args['completed'] ]
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
            response = {"message": e.args}
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)
    # Must be list owner to alter/remove. Note that all items in a list remain after
    # the delete.
    @login_required
    def delete(self, userId, listId, itemId):
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
        sqlProcName = 'delItem'
        sqlProcArgs = (itemId, )
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
            response = ''
            responseCode = 204
        except Exception as e:
            response = {"message": e.args}
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

# End item.py
