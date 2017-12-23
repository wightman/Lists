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
            response = {'status': 'login required'}
            responseCode = 401
            return make_response(jsonify(response), responseCode)
        return func(*args, **kwargs)
    return function_wrapper

def admin_required(func):
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        # Not admin? We're done.
        if not 'userAdmin' in session:
            response = {'status': 'admin privileges required'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)
        return func(*args, **kwargs)
    return function_wrapper

# End.
