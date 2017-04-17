from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single user and lets you delete a user
class User(Resource):
    def get(self, userId):
        try:
            return 'single user get',200
            #return getUser(userId), 200
        except:
            return '',404
        finally:
            result= 'This is the end'
            #close dbConnection

    def delete(self, todo_id):
        try:
            return 'user delete', 204
            # delUser(userId)
        except:
            return '', 404#do nothing
        finally:
            #close dbConnection
            return '', 204

    def put(self, todo_id):
        #parse user data
        #args = parser.parse_args()
        #task = {'task': args['task']}
        #TODOS[todo_id] = task
        try:
            return 'user edit', 204
            # delUser(userId)
        except:
            return '', 404#do nothing
        finally:
            #close dbConnection
            return '', 204


# UserList
# shows a list of all users, and lets you POST to add new users
class Users(Resource):
    def get(self):
        try:
            return 'users list', 200
            #return getUsersAll(), 200
        except:
            return '[]',200
        finally:
            result= 'This is the end'
            #close dbConnection

    def post(self):
        #parse user data
        #if incomplete, problematic, return '',???
        #if unauthorized, return '', ???
        try:
            #call createUser(stuff)
            return 'user create', 201
        except:
            return '',500
        finally:
           result= 'This is the end'
           #close dbConnection
        #args = parser.parse_args()
        #todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        #odo_id = 'todo%i' % todo_id
        #TODOS[todo_id] = {'task': args['task']}
        #return TODOS[todo_id], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<userId>')


if __name__ == '__main__':
    app.run(debug=True, host="lists.hopto.org", port=61340)
