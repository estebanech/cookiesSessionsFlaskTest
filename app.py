from crypt import methods
from tabnanny import check
from flask import Flask, render_template, request, redirect, make_response, session

app = Flask(__name__) 
app.secret_key = "this_key_is_super_secret_for_this_assignment"

@app.route('/')
def home():
    mode = request.cookies.get('displayMode')
    dark_mode = False
    if mode == 'dark_mode':
        dark_mode = True
    logged = False
    if 'loggedIn' in session:
        logged = session['loggedIn']
    return render_template('home.html',dark_mode=dark_mode,logged=logged)
 
@app.route('/Auth', methods=['GET','POST'])
def table():
    mode = request.cookies.get('displayMode')
    dark_mode = False
    if mode == 'dark_mode':
        dark_mode = True
    logged = False
    if 'loggedIn' in session:
        logged = session['loggedIn']
    if request.method == 'GET':
        return render_template('auth.html',dark_mode=dark_mode,logged=logged)
    else:
        if request.form.get('log-out') == 'log-out':
            session['loggedIn'] = False
            logged = False
            return render_template('auth.html',error=False,dark_mode=dark_mode,logged=logged)
        else:
            if request.form.get('username') == 'CIS658' and request.form.get('password') == 'WebArchitectures':
                session['loggedIn'] = True
                logged = True
                return render_template('auth.html',error=False,dark_mode=dark_mode,logged=logged)
            else:
                return render_template('auth.html',error=True,dark_mode=dark_mode,logged=logged)

@app.route('/Settings', methods=['GET','POST'])
def form():
    mode = request.cookies.get('displayMode')
    dark_mode = False
    if mode == 'dark_mode':
        dark_mode = True
    logged = False
    if 'loggedIn' in session:
        logged = session['loggedIn']
    if request.method == 'GET':
        return render_template('settings.html',dark_mode=dark_mode,logged=logged)
    else:
        if request.form.get('dark_mode'):
            response = make_response(render_template('settings.html',dark_mode=True,logged=logged))
            response.set_cookie('displayMode','dark_mode')
            return response
        else:
            response = make_response(render_template('settings.html',dark_mode=False,logged=logged))
            response.set_cookie('displayMode','light_mode')
            return response


 
if __name__ == '__main__': 
    app.run(host="0.0.0.0",port=8080) 