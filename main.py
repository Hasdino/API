from flask import Flask,redner_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
import hiddenthings
from forms import RegistrationForm, LoginForm



app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}/{}".format(hiddenthings.dbuser,hiddenthings.dbpass,hiddenthings.dbhost,hiddenthings.dbname)
db=SQLAlchemy(app)




class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), unique=True,nullable=True)
    email = db.Column(db.String(120), unique=True)
    image_file=db.Column(db.String(20), nullable=True, default="default.jpg")
    password= db.Column(db.String(60),nullable=False)


    def __repr__(self):
        return f"User('{self.name}', 'self{self.email}' , '{self.image_file}')"





@app.route("/")
def index():
    return "<h1 style='color : red'>hello flask</h1>"



@app.get("/drinks")
def get_drinks():
    return "yodsd"
 





if __name__ == "__main__":
    app.run(debug=True)