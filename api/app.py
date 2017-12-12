#!/usr/bin/env python3
from flask import Flask, jsonify, abort, request, make_response, session
from flask_restful import reqparse, abort, Api, Resource
from flask_session import Session
from flask_cors import CORS # NEW FOR USING WEB PAGES
import ssl #include ssl libraries

import settings
from resources.users import Users
from resources.user import User
from resources.signin import Signin

####################################################################################
#
# Error handlers
#
@app.errorhandler(400) # decorators to add to 400 response
def not_found(error):
	return make_response(jsonify( { 'status': 'Bad request' } ), 400)

@app.errorhandler(404) # decorators to add to 404 response
def not_found(error):
	return make_response(jsonify( { 'status': 'Resource not found' } ), 404)

#
# Note that Once a list is created or "gotten" all edits are then
# done using the listId since it's really the unique ID
#

app = Flask(__name__, static_url_path="")
CORS(app)
# Set Server-side session config: Save sessions in the local app directory.
app.secret_key = settings.SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_NAME'] = 'Lists'
app.config['SESSION_COOKIE_DOMAIN'] = settings.APP_HOST
Session(app)

##
## Actually setup the Api resource routing here
##
api = Api(app)
api.add_resource(Root, '/')
api.add_resource(Signin,'/signin')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<userId>')
#api.add_resource(UserLists, '/users/<userId>/lists')
#api.add_resource(Lists, '/lists')
#api.add_resource(List, '/lists/<listId>')


if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)
