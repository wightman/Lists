from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from resources.users import Users
from resources.user import User

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

##
## Actually setup the Api resource routing here
##
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<userId>')


if __name__ == '__main__':
    app.run(debug=True, host="lists.hopto.org", port=61340)
