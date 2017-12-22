#
# Decorators for the lists application.
#
# Rick Wightman, Dec 2017.
#
from flask import jsonify, make_response
from flask import Flask, session
from flask_session import Session

from functools import wraps

def login_required(func):
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        # Not logged in? We're done.
        print('Entered login_required')
        if not 'userId' in session:
            response = {'status': 'login required'}
            responseCode = 401
            return make_response(jsonify(response), responseCode)
        print('Login detected')
        func(*args, **kwargs)
    return function_wrapper

def admin_required(func):
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        # Not admin? We're done.
        print('Entered admin_required')
        if not 'userAdmin' in session:
            response = {'status': 'admin privileges required'}
            responseCode = 403
            print('Non-admin detected')
            return make_response(jsonify(response), responseCode)
        print('Admin detected')
        func(*args, **kwargs)
    return function_wrapper

# End.
