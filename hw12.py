from datetime import datetime
import json
import sys

with open('/phonebook', 'w+') as file:
    phonebook = json.loads(file.read())

    while True:
        user_input = input('Enter command: ')   # format command name phone
        split_input = user_input.split()
        command = split_input[0]
        if len(split_input) > 1:
            name = split_input[1]
        if len(split_input) > 2:
            phone = split_input[2]

        if command == 'add':
            if phonebook.get(name) is None:
                phonebook[name] = phone
                file.write(json.dumps(phonebook))
            else:
                print(f'{name} already recorded')

        elif command == 'delete':
            del phonebook[name]
            file.write(json.dumps(phonebook))

        elif command == 'show':
            for name in phonebook:
                print(name, phonebook[name])

        elif command == 'stats':
            print(len(phonebook))

        elif command == 'list':
            print(phonebook.keys())

#### decorated function ###
from datetime import datetime
def decorator(my_func):
    def deco_func(*args,**kwargs):
        with open('/phonebook', 'w+') as file:
            print(my_func.__name__, file=file)
            print(datetime.now(), file=file)
            my_func()
        return
    return deco_func()


### Custom Exception ###

class MyCustomException(Exception):
    with open('/phonebook', 'w+') as file:
        print(datetime.now(), file=file)
        print('error occured', file=file)
    pass

raise MyException('Custom exception is occured')

