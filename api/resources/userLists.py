# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask_restful import reqparse
from flask import request, url_for, jsonify
import pymysql.cursors
import jsondate as json
import dbSettings

# UserList
# - post: create a new list record and return it's listId
# - get: return the set of list data for a given userId
#
class UserLists(Resource):
    def post(self, userId):
        sqlProcName = 'addUserList'
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('listName', required=True, help='required')
        parser.add_argument('listDescription', required=False, help='required')
        args = parser.parse_args()
        listName = args['listName']
        try:
            listDescription = args['listDescription']
        except NameError:
            listDescription = ""
        # open the sql connection and call the stored procedure
        dbConnection = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            with dbConnection.cursor() as cursor:
                cursor.callproc(sqlProcName,[userId, listName, listDescription])
                dbConnection.commit()
                result = cursor.fetchone()
                uri = request.url+url_for('lists')+'/'+str(result['LAST_INSERT_ID()'])
                resource = { 'uri': uri }
                print(resource)
            return json.dumps(resource),200
        except pymysql.MySQLError as e:
            # failure
            return '',404
        finally:
            #close dbConnection
            dbConnection.close()

    def get(self, userId):
        sqlProcName = 'getUserLists'
        # open the sql connection and call the stored procedure
        dbConnection = pymysql.connect(settings.DBHOST,
                            settings.DBUSER,
                            settings.DBPASSWD,
                            settings.DBDATABASE,
                            charset='utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor)
        try:
            with dbConnection.cursor() as cursor:
                cursor.callproc(sqlProcName,[userId])
                result = cursor.fetchall()
                # close the connection
            return json.dumps(result),200
        except pymysql.MySQLError as e:
            # failure
            return '',404
        finally:
            #close dbConnection
            dbConnection.close()
