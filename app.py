from flask import Flask, redirect, url_for, render_template, request  # query parameters
from flask import session #stay as single user throughout all pages. its also a dic data structure. its a global variable (the dic)
app = Flask(__name__)  # we will work on one instanse of the class Flask
app.secret_key = '123' #כשמגדירים סשן חייבים סיסמה סודית


@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():
    # return 'welcome to the main page'
    found = True  # משל לחיפוש אובייקט בבסיס נתונים
    if found:
        return render_template('index.html', name='matan')
    else:
        return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])  # only 'post' is not allowed
def about_func():
    # TODO
    # DO SOMTHING WITH DB
    return render_template('about.html',
                           profile={'name': 'matan', 'second_name': 'spiro'},
                           university='BGU',
                           degrees=['BSc', 'MSc'],
                           hobbies=('art', 'music', 'sql', 'flask', 'animals', 'web'))


@app.route('/catalog')  # נלמד בהמשך איך לעשות את זה יותר דינמי וגנרי שיקבל איזשהו משתנה
def catalog_func():
    # return 'welcome to catalog page'
    if 'user_inside' in session:
        if session['user_inside']:
            print('user_inside')
    if 'product' in request.args:  #there is a problem - the keys are null if user didnt click "submit", it doesnt matter if he filled the attributes
        product = request.args['product']  # name of input in forms are the keys of query parameters
        size = request.args['size']
        return render_template('catalog.html', product=product, size=size) #sending variables to the html page
    return render_template('catalog.html')  # this route is for reaching this page directly from header

@app.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username'] #this is how you get the data that was inserted in the form
        password = request.form['password']
        #DB
        found = True
        if found:
            session['username'] = username #dic['K']=V
            return redirect(url_for('home_func'))
        else:
            return render_template('login.html')

@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
