from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple list to simulate user authentication.
users = {"username": "password"}


# Define a route for the home page.
@app.route('/')
def home():
    return "Welcome to the Distributed Concurrent Application"


# Define a route for a login page.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            # Successful login, you can redirect to another page here.
            return "Login successful"
        else:
            return "Login failed"

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)


def read_numbers_file(n):
    my_list = []
    aux = 0
    with open(file='numbers.txt', mode='r') as my_file:
        for orice_altceva in my_file:
            if orice_altceva.strip().isnumeric():
                my_list.append(orice_altceva.strip())
            else:
                print('This file is bad!')
            aux += 1
            if aux == n:
                return my_list
        return my_list