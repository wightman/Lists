#!/usr/bin/env python3
#
# Main application for lists.
#
# Rick Wightman, Dec 2016 -
#

from flask import Flask, jsonify, abort, request, make_response, session
from flask_restful import reqparse, abort, Api, Resource
from flask_session import Session
from flask_cors import CORS # NEW FOR USING WEB PAGES
import ssl #include ssl libraries
import datetime
import appSettings

app = Flask(__name__, static_url_path="")
CORS(app)

####################################################################################
#
# Error handlers
#
@app.errorhandler(400) # decorators to add to 400 response
def bad_request(error):
	return make_response(jsonify( { 'status': 'Bad request' } ), 400)

@app.errorhandler(404) # decorators to add to 404 response
def not_found(error):
	return make_response(jsonify( { 'status': 'Resource not found' } ), 404)

@app.errorhandler(405) # decorators to add to 405 response
def method_not_allowed(error):
	return make_response(jsonify( { 'status': 'The method is not allowed for the requested URL.' } ), 405)


#
# Set Server-side session config: Save sessions in the local app directory.
# Invalidate login after 60 miutes of inactivity.
#
app.secret_key = appSettings.SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_NAME'] = 'Lists'
app.config['SESSION_COOKIE_DOMAIN'] = appSettings.APP_HOST
app.permanent_session_lifetime = datetime.timedelta(minutes=60)
Session(app)

# Return the client application
class Root(Resource):
	def get(self):
		return app.send_static_file('index.html')

# Return the documentation
class Docs(Resource):
	def get(self):
		return app.send_static_file('docs.html')

#
# Delayed imports so they know about the app.
#
from resources.users import Users
from resources.user import User
from resources.signin import Signin
from resources.admin import Admin
from resources.password import Password
from resources.lists import Lists
from resources.list import List
from resources.collaborators import Collaborators
from resources.collaborator import Collaborator
from resources.accesstypes import AccessTypes
from resources.collaborations import Collaborations
from resources.collaboration import Collaboration
from resources.items import Items
from resources.item import Item
#
# Api resource routing: assign objects to endpoints
#
api = Api(app)
#api.add_resource(Root, '/')
#api.add_resource(Docs, '/docs')
api.add_resource(Signin,'/signin')
api.add_resource(Admin, '/admin/<int:userId>')
api.add_resource(Password, '/password')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:userId>')
api.add_resource(Lists, '/users/<int:userId>/lists')
api.add_resource(List, '/users/<int:userId>/lists/<int:listId>')
api.add_resource(Collaborators, '/users/<int:userId>/lists/<int:listId>/collaborators')
api.add_resource(Collaborator, '/users/<int:userId>/lists/<int:listId>/collaborators/<int:collaboratorId>')
api.add_resource(AccessTypes, '/accesstypes')
api.add_resource(Collaborations, '/users/<int:userId>/collaborations')
api.add_resource(Collaboration, '/users/<int:userId>/collaborations/<int:listId>')
api.add_resource(Items, '/users/<int:userId>/lists/<int:listId>/items')
api.add_resource(Item, '/users/<int:userId>/lists/<int:listId>/items/<int:itemId>')

context = ('cert.pem', 'key.pem') # Identify the certificates you've generated.


#
# Run the application
#
if __name__ == '__main__':
	app.run(
		host=appSettings.APP_HOST,
		port=appSettings.APP_PORT,
		ssl_context=context,
		debug=appSettings.APP_DEBUG
	)

# End app.py
