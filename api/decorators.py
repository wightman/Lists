#
# Decorators for the lists application.
#
# Rick Wightman, Dec 2017.
#
from functools import wraps

def login_required(func):
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        # Not logged in? We're done.
        if not 'userid' in session:
            response = {'status': 'login required'}
            responseCode = 401
            return make_response(jsonify(response), responseCode)
        return func(*args, **kwargs)
    return function_wrapper

def admin_required(func):
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        # Not admin? We're done.
        if not 'admin' in session:
            response = {'status': 'admin privileges required'}
            responseCode = 403
            return make_response(jsonify(response), responseCode)
        return func(*args, **kwargs)
    return function_wrapper

# End.
