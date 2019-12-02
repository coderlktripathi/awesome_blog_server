import bcrypt
from uuid import uuid4
from datetime import datetime



def generate_guid():
    guid = 'guid:{}:{}'
    uid = str(uuid4())

    t = datetime.today()
    return guid.format(t.isoformat(), uid)


def calculate_age(dob):
    today = datetime.today()

    try:
        b_date = datetime.strptime('dob', '%Y/%m/%d').strftime('%Y-%m-%d')
        return today.year - b_date.year
    except ValueError:
        print('Invalid date format')
    return None

def get_hash(input_str, salt=12):
    return bcrypt.hashpw(input_str.encode('UTF-8'), bcrypt.gensalt(salt)).decode('UTF-8')


def check_hash(input_str, hashed_str):
    return bcrypt.checkpw(input_str.encode(), hashed_str.encode())
