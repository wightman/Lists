# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask_restful import reqparse
import pymysql.cursors
import jsondate as json
import settings

# Todo
# shows a single user and lets you delete a user
class User(Resource):
    def get(self, userId):
        sqlProcName = 'getUser'
        # open the sql connection and call the stored procedure
        db = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            with db.cursor() as cursor:
                cursor.callproc(sqlProcName,[userId])
                result = cursor.fetchone()
                print(json.dumps(result))
                # close the connection
            return json.dumps(result),200
        except pymysql.MySQLError as e:
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
