#!/usr/bin/env python3
from flask import Flask, jsonify, abort, request, make_response, session
from flask_restful import reqparse, abort, Api, Resource
from flask_session import Session
from flask_cors import CORS # NEW FOR USING WEB PAGES
import ssl #include ssl libraries
import datetime

import settings
from resources.root import Root
from resources.users import Users
from resources.user import User
from resources.signin import Signin

app = Flask(__name__, static_url_path="")
CORS(app)

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
# Set Server-side session config: Save sessions in the local app directory.
# Invalidate login after 60 miutes of inactivity.
#
app.secret_key = settings.SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_NAME'] = 'Lists'
app.config['SESSION_COOKIE_DOMAIN'] = settings.APPHOST
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
# Api resource routing: assign objects to endpoints
#
api = Api(app)
api.add_resource(Root, '/')
api.add_resource(Docs, '/docs')
api.add_resource(Signin,'/signin')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<userId>')
#api.add_resource(UserLists, '/users/<userId>/lists')
#api.add_resource(Lists, '/lists')
#api.add_resource(List, '/lists/<listId>')


#
# Run the application
#
if __name__ == '__main__':
    app.run(debug=settings.APPDEBUG, host=settings.APPHOST, port=settings.APPPORT)

# End.
