from flask_restful import Resource


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
