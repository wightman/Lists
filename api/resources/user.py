from flask_restful import Resource

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
