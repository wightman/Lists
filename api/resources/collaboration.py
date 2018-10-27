# -*- coding: utf-8 -*-
from flask import Flask, session, jsonify, abort, request, make_response, url_for
from flask_restful import Resource, reqparse, abort
from flask_session import Session
import pymysql.cursors
import dbSettings
from decorators import login_required, admin_required

import jsondate as json
from pymysql.err import IntegrityError

# Collaborations
# Users can discover their collaborations
class Collaboration(Resource):
    @login_required
    def get(self, userId, listId):
        if userId != session['userId']:
            response = {'message': 'users can only see their own collaborations'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)
        sqlProcName = 'getCollaboration'
        sqlProcArgs = (userId,listId)
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
            response['uri']  = url_for('list', userId = response['ownerId'], listId = response['listId'],
                _external=True)
            responseCode = 200
        except Exception as e:
            response = {"status": e.args[1]}
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

    @login_required
    def get(self, userId, listId):
        if userId != session['userId']:
            response = {'message': 'users can only see their own collaborations'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)
        sqlProcName = 'getCollaboration'
        sqlProcArgs = (userId,listId)
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
            response['uri']  = url_for('list', userId = response['ownerId'], listId = response['listId'],
                _external=True)
            responseCode = 200
        except Exception as e:
            response = {"status": e.args[1]}
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

    @login_required
    def put(self, userId, listId):
        if userId != session['userId']:
            response = {'message': 'users can only see their own collaborations'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)
        # Users can change their collaborationViewed flag.
        sqlProcName = 'putCollaboration'
        sqlProcArgs = ()
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
            response = cursor.commit()
            responseCode = 204
        except Exception as e:
            response = {"status": e.args[1]}
            responseCode = 404
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)


# End Collaboration.py
