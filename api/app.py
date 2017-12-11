#!/usr/bin/env python3
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import settings
from resources.users import Users
from resources.user import User
from resources.signin import Signin

#
# Note that Once a list is created or "gotten" all edits are then
# done using the listId since it's really the unique ID
#
#from resources.userLists import UserLists
#from resources.lists import Lists
#from resources.list import List

app = Flask(__name__)
api = Api(app)

##
## Actually setup the Api resource routing here
##
api.add_resource(Signin,'/signin')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<userId>')
#api.add_resource(UserLists, '/users/<userId>/lists')
#api.add_resource(Lists, '/lists')
#api.add_resource(List, '/lists/<listId>')


if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)
