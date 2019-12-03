# src/shared/Authentication
import jwt
import datetime
from flask import make_response, current_app as app
from eve.auth import TokenAuth


class JwtAuth(TokenAuth):
    """
    Auth Class
    """
    def check_auth(self, token, allowed_roles, resource, method):
        users = app.data.driver.db['users']
        if users.find_one({'token': token}):
            decoded_data = JwtAuth.decode_token(token)
            if decoded_data.get('user_id'):
                return True
        return False

    @staticmethod
    def generate_token(user_id):
        """
        Generate Token Method
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config['SECRET_KEY'],
                'HS256'
            ).decode("utf-8")
        except Exception:
            return make_response(
                {'error': 'error in generating user token'},
                400
            )

    @staticmethod
    def decode_token(token):
        """
        Decode token method
        """
        re = {'user_id': None, 'error': {}}
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'])
            re['user_id'] = payload['sub']
            return re
        except jwt.ExpiredSignatureError:
            re['error'] = {'message': 'token expired, please login again'}
            return re
        except jwt.InvalidTokenError:
            re['error'] = {'message': 'Invalid token, please try again with a new token'}
            return re

    @staticmethod
    def create_response_user(user):
        for key in ('_id', 'password', 'token'):
            del user[key]
        return user
