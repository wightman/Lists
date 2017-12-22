# -*- coding: utf-8 -*-
from flask import jsonify, abort, request, make_response
from flask_restful import Resource, reqparse, abort
from flask import Flask, session
from flask_session import Session
import pymysql.cursors
import settings
from decorators import login_required, admin_required

# Create, check and remove signins to the service
class Signin(Resource):
#    def __init__(**kwargs):
#        self.session = kwargs['session']

    #
    # Create a signin.
    # Example curl command:
	# curl -i -H "Content-Type: application/json" -X POST -d '{"userEmail": "TheNewYou@example.ca", "password": "$FAIL0$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a"}'
    #  	 -c cookie-jar http://lists.hopto.org:61340/signin
	#
    def post(self):
        if not request.json:
            abort(400) # bad request
        # Parse the json
        parser = reqparse.RequestParser()
        response = {'status': 'Internal Server Error'}
        responseCode = 500
        try:
            # Check for required attributes in json document, create a dictionary
            parser.add_argument('userEmail', type=str, required=True)
            parser.add_argument('password', type=str, required=True)
            request_params = parser.parse_args()
        except:
            abort(400) # bad request
        sqlProcName = 'verifyUser'
        sqlProcArgs = [request_params['userEmail'], request_params['password']]
        # open the sql connection and call the stored procedure
        db = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            cursor = db.cursor()
            cursor.callproc(sqlProcName,sqlProcArgs)
            response = cursor.fetchone()
            # At this point we have sucessfully authenticated.
#            print(response)
            session['userId'] = response['userId']
            session['userAdmin'] = response['userAdmin']
            responseCode = 201
        except pymysql.MySQLError as e:
            response = {'status': 'Access denied'}
            responseCode = 403
        finally:
            #close dbConnection
            db.close()
            return make_response(jsonify(response), responseCode)

	# GET: Check Cookie data with Session data
	#
    # Example curl command:
	# curl -i -H "Content-Type: application/json" -X GET -b cookie-jar
	#	-k http://lists.hopto.org:61340/signin
    def get(self):
        if 'userId' in session:
            response = {'status': 'success'}
            responseCode = 200
        else:
            response = {'status': 'fail'}
            responseCode = 403
        return make_response(jsonify(response), responseCode)

	# DELETE: Check Cookie data with Session data
	#
	# Example curl command:
	# curl -i -H "Content-Type: application/json" -X DELETE -b cookie-jar
	#	-k http://lists.hopto.org:61340/signin
    def delete(self):
        if 'userid' in session:
            session.pop('logged_in', None)
            response = {'status': 'success'}
            responseCode = 204
        else:
            response = {'status': 'fail'}
            responseCode = 404
        return make_response(jsonify(response), responseCode)
# End.
