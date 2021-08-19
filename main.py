from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml

app=Flask(__name__)



app.config["MYSQL_HOST"]=
app.config['MYSQ;_USER']="
app.config['MYSQL_PASSWORD']="
app.config["MYSQL_DB"]= "

mysql=MySQL(app)


@app.route('/', methods =["GET" , "POST"])
def index():
	if request.method =="POST":
		userDetails= request.form
		name= userDetails["name"]
		email= userDetails["email"]
		cur = mysql.connection.cursor()
		cur.execute(" INSERTINSERT INTO users(name,email) VALUES(%s, %s)",(name,email))
		mysql.connection.commit()
		cur.close()
		return "sucess"

	return render_template("index.html")

if __name__ == '__main__':
	app.debug = True
	app.run()