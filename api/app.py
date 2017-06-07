# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import settings
from resources.users import Users
from resources.user import User
from resources.lists import Lists

app = Flask(__name__)
api = Api(app)

##
## Actually setup the Api resource routing here
##
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<userId>')
api.add_resource(Lists, '/users/<userId>/lists')


if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)
