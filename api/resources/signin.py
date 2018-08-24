# -*- coding: utf-8 -*-
from flask import jsonify, abort, request, make_response
from flask_restful import Resource, reqparse, abort
from flask import Flask, session
from flask_session import Session
import pymysql.cursors
import dbSettings
from decorators import login_required, admin_required

# Create, check and remove signins to the service
class Signin(Resource):

    #
    # Create a signin.
    # Example curl command:
	# curl -i -H "Content-Type: application/json" -X POST -d
    #   '{"userEmail": "TheNewYou@example.ca", "userPassword":
    #   "$FAIL0$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a"}'
    #  	 -c cookie-jar https://lists.hopto.org:61340/signin
	#
    def post(self):
        if not request.json:
            abort(400) # bad request
        # Parse the json
        response = {'status': 'Internal Server Error'}
        responseCode = 500
        try:
            # Check for required attributes in json document, create a dictionary
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument('userEmail', type=str,
                required=True, help='user email address is required')
            parser.add_argument('userPassword', type=str,
                required=True, help='user password is required')
            args = parser.parse_args()
        except Exception as e:
            abort(400, error='unable to parse request') # bad request
        sqlProcName = 'verifyUser'
        sqlProcArgs = [args['userEmail'], args['userPassword'].encode()]
        # open the sql connection and call the stored procedure
        dbConnection = pymysql.connect(
            dbSettings.DB_HOST,
            dbSettings.DB_USER,
            dbSettings.DB_PASSWD,
            dbSettings.DB_DATABASE,
            charset='utf8mb4',
            cursorclass= pymysql.cursors.DictCursor
        )
        try:
            cursor = dbConnection.cursor()
            cursor.callproc(sqlProcName,sqlProcArgs)
            response = cursor.fetchone()
            # At this point we have sucessfully authenticated.

            # the db query returns 1 for True and 0 for False for userAdmin.
            #   This is bad, so we fix it.
            session['userId'] = response['userId']
            if response['userAdmin'] == 1:
                session['userAdmin'] = True
            else:
                session['userAdmin'] = False
            responseCode = 201
        except pymysql.MySQLError as e:
            response = {'message': 'Can\'t touch this.'}
            responseCode = 403
        finally:
            #close dbConnection
            dbConnection.close()
            return make_response(jsonify(response), responseCode)

	# DELETE: Check Cookie data with Session data
	#
	# Example curl command:
	# curl -i -H "Content-Type: application/json" -X DELETE -b cookie-jar
	#	-k http://lists.hopto.org:61340/signin
    def delete(self):
        if 'userId' in session:
            session.pop('userId', None)
            response = {'message': 'Logout successful.'}
            responseCode = 204
        else:
            response = {'message': 'Logout failed.'}
            responseCode = 404
        return make_response(jsonify(response), responseCode)

# End signin.py
