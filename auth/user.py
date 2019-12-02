from service import BaseService
from resource import Resource
from .common import generate_guid, get_hash, calculate_age


class UserResource(Resource):
    schema = {
        'firstname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'lastname': {
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
            'unique': True,
            'readonly': True,
        },
        'age': {
            'type': 'integer',
            'readonly': True,
        },
        'admin': {
            'type': 'boolean',
            'default': False
        },
        # 'location': {
        #     'type': 'dict',
        #     'schema': {
        #         'address': {'type': 'string'},
        #         'city': {'type': 'string'}
        #     },
        # },
        'dob': {
            'type': 'string',
        },
        'password': {
            'type': 'string',
            'minlength': 5,
        }
        # 'email': {'type': 'email'}
    }

    resource_title = 'user'
    resource_methods = ['GET', 'POST']
    item_methods = ['GET', 'PUT', 'PATCH', 'DELETE']

    additional_lookup = {
        'url': 'regex("[\w,.:-]+")',
        'field': 'guid'
    }

    datasource = {
        'default_sort': [('username', 1)],
        'projection': {
            'password': 0,
            '_id': 0
        }
    }


class UserService(BaseService):
    def on_create(self, docs):
        for doc in docs:
            if not doc.get('guid'):
                doc['guid'] = generate_guid()
            if doc.get('password'):
                doc['password'] = get_hash(doc['password'])
            if doc.get('dob'):
                doc['age'] = calculate_age(doc['dob'])
