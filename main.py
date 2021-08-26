from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import hiddenthings
import pymysql
from flask import Flask, render_template, flash, request, redirect, url_for
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}/{}".format(hiddenthings.dbuser,hiddenthings.dbpass,hiddenthings.dbhost,hiddenthings.dbname)
db=SQLAlchemy(app)


#our model
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
 
 
    def __init__(self, username, password):
        self.username = username
        self.password = password
 
 
 
 
 
 
 
#creating our routes
@app.route('/')
def index():
 
    return render_template('index.html')
 
 
 
#login route
@app.route('/login' , methods = ['GET', 'POST'])
def Login():
    form = LoginForm()
 
    if form.validate_on_submit():
        if request.form['username'] != 'codeloop' or request.form['password'] != '12345':
            flash("Invalid Credentials, Please Try Again")
 
 
        else:
            return redirect(url_for('index'))
 
 
 
    return render_template('login.html', form = form)
 
 
 
 
 
#run flask app
if __name__ == "__main__":
    app.run(debug=True)