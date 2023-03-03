### decorated function ###
from datetime import datetime
def decorator(my_func):
    def deco_func(*args, **kwargs):
        print(my_func.__name__)
        print(datetime.now())
        return my_func(*args, **kwargs)
    return deco_func()

@decorator
def print_func():
    print('This is my function')


### Custom Exception ###
class MyCustomException(Exception):
    pass

raise MyException('Custom exception is occured')

### Context Manager ###
class ContextManager():
    def __init__(self, value):
        self.value = value
    def __enter__(self):
        print('==========')
        return self
    def __exit__(self, exc_type, exc_value, exc_trb):
        if exc_type is not None:
            print(f'Error due to exception {exc_value}')
        print(f'This was a value {self.value}')
        print('==========')
        return True

with ContextManager(1) as some_value:
    print(f'Some Value is {some_value}')


### try, except ###
try:
    print('==========')
    some_value = 1
    print(f'Some Value is {some_value}')
except Exception as e:
    print(f'Error due to exception {e}')
finally:
    print(f'This was a value {self.value}')
    print('==========')
