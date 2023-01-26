# people.py

from datetime import datetime
from flask import abort

def get_timestamp():
    return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))

# Why is this a dictionary, and not an array ?
data = {
    'Jigoro': {
        'fname': 'Kano',
        'lname': 'Jigoro',
        'timestamp': get_timestamp(),
    },
    'Funakoshi': {
        'fname': 'Gichin',
        'lname': 'Funakoshi',
        'timestamp': get_timestamp(),
    },
    'Ueshiba': {
        'fname': 'Morihei',
        'lname': 'Ueshiba',
        'timestamp': get_timestamp(),
    },
}

def read_all():
    return list(data.values())

def read_one(lname):
    if lname in data:
        return data[lname]
    else:
        abort(404, f'Person with last name "{lname}" not found')

def create(person):
    print(person)
    lname = person.get('lname')
    fname = person.get('fname')

    if lname not in data:
        data[lname] = {
            'lname': lname,
            'fname': fname,
            'timestamp': get_timestamp(),
        }
        return data[lname], 201
    else:
        abort(406, f'Person with last name "{lname}" already exists')