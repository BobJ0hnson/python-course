from flask import Flask
import random

# 1 request to endpoint /users returns a random list of names
app = Flask(__name__)

names = ['Bob', 'John', 'Jack', 'Suzie', 'Heidi']

@app.route('/users')
def get_users():
    random.shuffle(names)
    return names

if __name__ == '__main__':
    app.run()

# request to endpoint /books returns a random number of books as a html list

app = Flask(__name__)

bnames = ['Neuromancer', 'Count Zero', 'Mona Lisa Overdrive', 'Johnny Mnemonic']

# define a route to handle GET requests to "/books"
@app.route('/books')
def get_books():
    # select num_names random names from the list
    num_names = random.randint(1, 5)
    random_names = random.sample(bnames, num_names)

    # create an HTML unordered list
    html_list = '<ul>' + ''.join(['<li>{}</li>'.format(bnames) for name in bnames]) + '</ul>'
    
    return html_list

if __name__ == '__main__':
    app.run()

# request to endpoint GET /users and /books with parameters:

from flask import Flask, abort
import re

@app.route('/users/<int:id>')
def get_user(id):
    # check if id is divisible by 2
    if id % 2 == 0:
        dev_id = id % 2
        return f"{id} devided by 2 is {dev_id}"
    else:
        abort(404)

@app.route('/books/<title>')
def get_book(title):
    # capitalize the first letter of the title
    title = title.capitalize()

    return title

if __name__ == '__main__':
    app.run()


#  GET requests to "/params" to return keys and values in html table

from flask import Flask, request
app = Flask(__name__)

@app.route('/params')
def get_params():
    query_params = request.args.to_dict()

    html_table = '<table><tr><th>parameter</th><th>value</th></tr>'

    for key, value in query_params.items():
        html_table += f'<tr><td>{key}</td><td>{value}</td></tr>'
    html_table += '</table>'

    return html_table

if __name__ == '__main__':
    app.run()


#  GET, POST requests to "/login" to check auth data

from flask import Flask, request, redirect, abort

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def show_login_form():
    
    return '''
        <form method="POST" action="/login">
            <label>Username:</label>
            <input type="text" name="username"><br>
            <label>Password:</label>
            <input type="password" name="password"><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/login', methods=['POST'])
def process_login_form():
    # check if the request contains data for 'username' and 'password'
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:
        return redirect('/users')
    else:
        abort(400, 'username and password not found')


@app.route('/users')
def show_users_page():
    # render a users page
    return '<h1>Welcome to the Users Page!</h1>'

if __name__ == '__main__':
    app.run()