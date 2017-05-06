from flask_restful import Resource
from flask_restful import reqparse
import pymysql.cursors
import jsondate as json

# UserList
# shows a list of all users, and lets you POST to add new users
class Users(Resource):
    def get(self):
        sqlProcName = 'getUsersAll'
        # open the sql connection and call the stored procedure
        db = pymysql.connect(host='localhost',
                            user='wightman',
                            passwd='JesusL0vesMe!',
                            db='lists',
                            charset='utf8',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            with db.cursor() as cursor:
                cursor.callproc(sqlProcName)
                result = cursor.fetchall()
                print(json.dumps(result))
                # close the connection
            return json.dumps(result),200
        except:
            # failure
            return '',404
        finally:
            #close dbConnection
            db.close()

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
