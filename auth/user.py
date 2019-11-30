from service import BaseService
from resource import Resource


class UserResource(Resource):
    schema = {
        'firstname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'lasttname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'username': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'required': True,
            'unique': True,
        },
        'guid': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'age': {
            'type': 'int',
            'readonly': True,
        },
        'admin': {
            'type': 'boolean',
            'default': False
        },
        'location': {
            'type': 'dict',
            'schema': {
                'address': {'type': 'string'},
                'city': {'type': 'string'}
            },
        },
        'dob': {
            'type': 'datetime',
        },
        'email': {'type': 'email'}
    }

    resource_title = 'user'
    resource_methods = ['GET', 'POST']
    item_methods = []


class UserService(BaseService):
    def on_fetched(self, doc):
        pass
