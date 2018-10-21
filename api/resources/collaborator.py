# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response, url_for
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import dbSettings
from decorators import login_required, admin_required

import jsondate as json
from pymysql.err import IntegrityError

class Collaborator(Resource):
    # List collaborators can get collaboration information about members
    @login_required
    def get(self, userId, listId, collaboratorId):
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
        sqlProcName = 'getCollaborator'
        sqlProcArgs = (collaboratorId, listId)
        try:
            cursor = db.cursor()
            cursor.callproc(sqlProcName, sqlProcArgs)
            response = cursor.fetchone()
            response['uri']  = url_for('collaborators', userId = userId, listId = listId,
                _external=True) + '/' + str(response['collaboratorId'])
            responseCode = 200
        except Exception as e:
            response = {"status": e.args[1]}
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

@login_required
def put(self, userId, listId, collaboratorId):
    if userId != session['userId']:
        response = {'message': 'Only list owners can alter collaborations'}
        responseCode = 403
        return make_response(jsonify(response), responseCode)
    sqlProcName = 'putCollaborator'
    # parse user data
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('accessType', type=str, location='json',
        required=True, help='An access type is required.')
    args = parser.parse_args()
    sqlProcArgs = [collaboratorId, listId, args['accessType'] ]
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
        responseCode = 500
    finally:
        #close dbConnection
        db.close()
        return make_response(jsonify(response), responseCode)

# Must be list owner to alter/remove. Note that all items in a list remain after
# the delete.
    @login_required
    def delete(self, userId, listId, collaboratorId):
        if userId != session['userId']:
            response = {'message': 'Only list owners can remove collaborations'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)
        sqlProcName = 'delCollaborator'
        sqlProcArgs = (collaboratorId, listId)
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
            responseCode = 403
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

# End collaborator.py
