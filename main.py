from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml

app=Flask(__name__)



if __name__ == '__main__':
	app.debug = True
	app.run()