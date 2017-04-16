# getDB; Rick Wightman; Apil 2017
#
# Trial to get data using MySQLdb into a dictionary object and then convert to
# json using marshmallow
from marshmallow import Schema, fields, post_load
import MySQLdb

class User(object):
    def __init__(self, id, name, email, admin, created, uri):
        self.userId = id            #read-only, db generated
        self.userName = name
        self.userEmail = email
        self.userAdmin = admin
        self.userSince = created    #read-only, db generated
#        self.userUri = uri          #read-only, app generated

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)

class UserSchema(Schema):
    userId = fields.Integer()       #read-only, db generated
    userName = fields.Str()
    userEmail = fields.Email()
    userAdmin = fields.Boolean()
    userSince = fields.DateTime()   #read-only, db generated
#    userUri = fields.Uri()          #read-only, app generated

    # Enable deserializing to a User object
    @post_load
    def make_user(self, data):
        return User(**data)

db = MySQLdb.connect(host='localhost', user='wightman', passwd='JesusL0vesMe!', db='lists', cursorclass=MySQLdb.cursors.DictCursor)
cursor = db.cursor()
cursor.callproc('getUsersAll')
data = cursor.fetchone()
