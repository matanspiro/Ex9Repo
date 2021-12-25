from flask import Flask, redirect, url_for, render_template, request  # query parameters
from flask import session #stay as single user throughout all pages. its also a dic data structure. its a global variable (the dic)
app = Flask(__name__)
app.secret_key = '123' #כשמגדירים סשן חייבים סיסמה סודית


@app.route('/home')
@app.route('/')
def home_func():
    return render_template('home.html')


@app.route('/assignment9', methods=['GET', 'POST'])
def ass9_func():
    if request.method == 'GET':
        users = {'user1': {'Name': 'a', 'Email': 'a@gmail.com'},
                 'user2': {'Name': 'b', 'Email': 'b@gmail.com'},
                 'user3': {'Name': 'c', 'Email': 'c@gmail.com'},
                 'user4': {'Name': 'd', 'Email': 'd@gmail.com'},
                 'user5': {'Name': 'e', 'Email': 'e@gmail.com'}
                 }
        if 'name' in request.args:  #'name' is what's got transferred from the html file
            name = request.args['name']
            if name != '':
                session['name'] = name  #here i set the global variables, using session
                for i in users:
                    # i in 'users' means: getting the keys of 'users' (user1, user2...)
                    # users[i] means: get the values of 'users' (Name: a, Email: a@gmail.com) -> takes you to the values of the first dictionary
                    for j in users[i]:
                        # j means the keys of inner dictionary
                        if users[i][j] == name:
                            result = users[i]
                            session['result'] = result
                            #  users[i][j] gets the values of the inner dictionary
                            return render_template('assignment9.html', Name=name, Result=result)  # sending variables to the html page

            else:
                name = request.args['name']
                print('ggggg')
                return render_template('assignment9.html', Name=name, Users=users)

    if request.method == 'POST':
        username = request.form['username']  #  this is how you get the data that was inserted in the form
        password = request.form['password']
        session['username'] = username
        return redirect(url_for('ass9_func'))

    return render_template('assignment9.html')


@app.route('/log_out')
def logout_func():
    username = ''
    session['username'] = username
    return render_template('assignment9.html', Username=username)


if __name__ == '__main__':
    app.run(debug=True)
