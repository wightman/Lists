# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
import pymysql.cursors
import jsondate as json
from urllib.parse import unquote
from struct import *
import settings


# UserList
# shows a list of all users, and lets you POST to add new users
class Users(Resource):
    def get(self):
        sqlProcName = 'getUsersAll'
        # open the sql connection and call the stored procedure
        db = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            with db.cursor() as cursor:
                cursor.callproc(sqlProcName)
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
        sqlProcName = 'addUser'
        # parse user data
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name', required=True, help='required')
        parser.add_argument('email', required=True, help='required')
        parser.add_argument('passwd', required=True, help='required')
        parser.add_argument('admin', type=bool)
        args = parser.parse_args()
        passwd = args['passwd'].encode()
        try:
            admin
        except NameError:
            admin = False
        try:
            sqlProcArgs = [args['name'], args['email'], passwd, args['admin'] ]
        except TypeError as e:
            abort(400,e.message)

        print("args dict built")
        print(sqlProcArgs)
        # open the sql connection and call the stored procedure
        db = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor)
        print("connected")
        try:
            with db.cursor() as cursor:
                print(sqlProcArgs)
                cursor.callproc(sqlProcName, ['crappy', 'crappy@me.com',
                   pack('$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a'), 0] )
                cursor.commit()
                result = cursor.fetchone()
                print("procedure completed")
                uri = host + ':' + port + '/users/' + result['userId']
                print(json.dumps(uri))
                # close the connection
            return json.dumps(uri),201
#        except pymysql.err.InternalError as e:
        except Exception as e:
            return abort(500,message=e )
        finally:
            #close dbConnection
            db.close()
