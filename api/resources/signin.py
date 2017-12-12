# -*- coding: utf-8 -*-
from flask import jsonify, abort, request, make_response
from flask_restful import Resource, reqparse, abort
import pymysql.cursors
import jsondate as json
from urllib.parse import unquote
from struct import *
import settings


# Create, check and remove signins to the service
class Signin(Resource):
    #
    # Create a signin.
    # Example curl command:
	# curl -i -H "Content-Type: application/json" -X POST -d '{"userEmail": "TheNewYou@example.ca", "password": "$FAIL0$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a"}'
    #  	 http://lists.hopto.org:61340/signin
	#
    def post(self):
        if not request.json:
            abort(400) # bad request
        # Parse the json
        parser = reqparse.RequestParser()
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
			session['username'] = request_params['username']
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
	#	-k https://info3103.cs.unb.ca:61340/signin
#	def get(self):
#		if 'username' in session:
#			response = {'status': 'success'}
#			responseCode = 200
#		else:
#			response = {'status': 'fail'}
#			responseCode = 403

#		return make_response(jsonify(response), responseCode)

	# DELETE: Check Cookie data with Session data
	#
	# Example curl command:
	# curl -i -H "Content-Type: application/json" -X DELETE -b cookie-jar
	#	-k https://info3103.cs.unb.ca:61340/signin

	#
	#	Here's your chance to shine!
	#
