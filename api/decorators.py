#
# Decorators for the lists application.
#
# Rick Wightman, Dec 2017.
#
from flask import jsonify, request, make_response
from flask import Flask, session
from flask_session import Session

from functools import wraps

def login_required(func):
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        # Not logged in? We're done.
        if not 'userId' in session:
            response = {'message': 'login required'}
            responseCode = 401
            return make_response(jsonify(response), responseCode)
        return func(*args, **kwargs)
    return function_wrapper

def owner_required(func):
    @login_required
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        # Must be the owner user.
        if userId != session['userId']:
            response = {'message': 'Owner privileges are required.'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)
        return func(*args, **kwargs)
    return function_wrapper

def admin_required(func):
    @login_required
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        # Not admin? We're done.
        if session['userAdmin'] is not True:
            print(session['userAdmin'])
            response = {'message': 'Admin privileges are required.'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)
        return func(*args, **kwargs)
    return function_wrapper

def privilege_required(func):
    @login_required
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        # Must be admin or the owner user
        if session['userAdmin'] is not True and userId != session['userId']:
            response = {'message': 'Admin or owner privileges are required.'}
            responseCode = 403
        return func(*args, **kwargs)
    return function_wrapper

# End decorators.py
