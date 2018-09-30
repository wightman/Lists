#!/usr/bin/env python3

import pymysql.cursors
import dbSettings
sqlProcName = 'verifyUser'
sqlProcArgs = ('TheNewYou@example.ca','$FAIL0$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a')
#sqlProcArgs = ('you@unb.ca','$2y$12$fNRkFdY6UsdRZ3MQgYOgLe6KhJg74Roc2Z3j.VxncdcBhnMiJU0jS')
response = {'status': 'Internal Server Error'}
responseCode = 500
db = pymysql.connect(
    dbSettings.DB_HOST,
    dbSettings.DB_USER,
    dbSettings.DB_PASSWD,
    dbSettings.DB_DATABASE,
    charset='utf8mb4',
    cursorclass= pymysql.cursors.DictCursor
    )
try:
    responseCode = 500
    cursor = db.cursor()
    cursor.callproc(sqlProcName,sqlProcArgs)
    response = cursor.fetchone()
    db.commit()
    # At this point we have sucessfully authenticated.
    responseCode = 201
except pymysql.err.InternalError  as e:
    response = {'message': e.args}
    responseCode = 403
finally:
    #close dbConnection
    db.close()
    print(response)
    print(responseCode)
