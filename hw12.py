from datetime import datetime
import json
import sys


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
                with open('phonebook', 'w+') as file:
                    file.write(json.dumps(phonebook))
                        else:
                            print(f'{name} already recorded')

        elif command == 'delete':
            if phonebook.get(name) is not None:
                del phonebook[name]
                with open('phonebook', 'w+') as file:
                    file.write(json.dumps(phonebook))
            else: 
                print(f'{name} not found')

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
        with open('phonebook_log', 'a') as file:
            print(my_func.__name__, file=file)
            print(datetime.now(), file=file)
            my_func(*args, **kwargs)
        return
    return deco_func


### Custom Exception ###

class MyCustomException(Exception):
    with open('phonebook_log', 'a') as file:
        print(datetime.now(), file=file)
        print('error occured', file=file)
    pass

raise MyException('Custom exception is occured')

