# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
import pymysql.cursors
import jsondate as json
from urllib.parse import unquote
from struct import *
import settings


# Lists
# shows all listsfor a user, and lets a user POST to add new lists
class Lists(Resource):
    def get(self,userId):
        sqlProcName = 'getUserLists'
        # open the sql connection and call the stored procedure
        db = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            with db.cursor() as cursor:
                cursor.callproc(sqlProcName,[userId])
                result = cursor.fetchall()
                print(json.dumps(result))
                # close the connection
            return json.dumps(result),200
        except pymysql.MySQLError as e:
            return abort(404,message=unquote(e.args[1]) )
        finally:
            #close dbConnection
            db.close()

    def post(self):
        sqlProcName = 'addList'
        # parse user data
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('userId', type=int,required=True, help='required')
        parser.add_argument('listName', required=True, help='required')
        parser.add_argument('listDescription', required=True, help='required')
        args = parser.parse_args()
        try:
            sqlProcArgs = [args['userId'], args['listName'],
            args['listDescription'] ]
        except TypeError as e:
            abort(400,e.message)

        print("args dict built")
        print(sqlProcArgs)
        # open the sql connection and call the stored procedure
        db = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8',
                            cursorclass= pymysql.cursors.DictCursor)
        print("connected")
        try:
            with db.cursor() as cursor:
                print(sqlProcArgs)
                cursor.callproc(sqlProcName, sqlProcArgs)
                cursor.commit()
                result = cursor.fetchone()
                print("procedure completed")
                uri = host + ':' + port + '/lists/' + result['listId']
                print(json.dumps(uri))
                # close the connection
            return json.dumps(uri),201
#        except pymysql.err.InternalError as e:
        except Exception as e:
            return abort(500,message=e )
        finally:
            #close dbConnection
            db.close()
