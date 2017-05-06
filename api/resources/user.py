from flask_restful import Resource
from flask_restful import reqparse
import pymysql.cursors
import jsondate as json

# Todo
# shows a single user and lets you delete a user
class User(Resource):
    def get(self, userId):
        sqlProcName = 'getUser'
        parser = reqparse.RequestParser()
        parser.add_argument('userId')
        print(userId)
        # open the sql connection and call the stored procedure
        db = pymysql.connect(host='localhost',
                            user='wightman',
                            passwd='JesusL0vesMe!',
                            db='lists',
                            charset='utf8',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            with db.cursor() as cursor:
                cursor.callproc(sqlProcName,[userId])
                result = cursor.fetchone()
                print(json.dumps(result))
                # close the connection
            return json.dumps(result),200
        except:
            # failure
            return '',404
        finally:
            #close dbConnection
            db.close()

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
