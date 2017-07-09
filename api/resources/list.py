# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
import pymysql.cursors
import jsondate as json
from urllib.parse import unquote
from struct import *
import settings


# Lists
# - put: modify (replace the data for) a list
# - delete: remove a list
class List(Resource):
    def put(self, listId):
        sqlProcName = 'putList'
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('listName', required=True, help='required')
        parser.add_argument('listDescription', required=True, help='required')
        args = parser.parse_args()
        listName = args['listName']
        listDescription = args['listDescription']
        # open the sql connection and call the stored procedure
        dbConnection = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            with dbConnection.cursor() as cursor:
                cursor.callproc(sqlProcName,[listId, listName, listDescription])
                dbConnection.commit()
                result = cursor.fetchone()
            return '',200
        except pymysql.IntegrityError:
            return ListName + 'already exists', 403
        except pymysql.MySQLError as e:
            # failure
            return '',404
        finally:
            #close dbConnection
            dbConnection.close()

    def delete(self, listId):
        print("here!")
        sqlProcName = 'delList'
        dbConnection = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            with dbConnection.cursor() as cursor:
                cursor.callproc(sqlProcName,[listId])
                dbConnection.commit()
            return '',200
        except pymysql.MySQLError as e:
            # failure
            return '',404
        finally:
            #close dbConnection
            dbConnection.close()
