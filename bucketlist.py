from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password, please try again'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect('login')
    return render_template('signup.html')


@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

