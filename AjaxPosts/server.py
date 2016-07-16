from flask import Flask, render_template, request, redirect, Markup
from mysqlconnection import MySQLConnector

app=Flask(__name__)
mysql=MySQLConnector(app,'myownapi')


@app.route('/')
def index():
	select_query = "SELECT * FROM posts"
	posts = mysql.query_db(select_query)
	
	return render_template('index.html',posts=posts)


@app.route('/create',methods=['POST'])
def create():
	query = "INSERT INTO posts (description) VALUES('{}')".format(request.form['newpost'])
	mysql.query_db(query)
	
	select_query = "SELECT * FROM posts"
	posts = mysql.query_db(select_query)

	# return redirect('/')
	return render_template('index.html',posts=posts)

app.run(debug=True)