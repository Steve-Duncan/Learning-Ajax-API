from flask import Flask, render_template, request, redirect, jsonify
from mysqlconnection import MySQLConnector

app=Flask(__name__)
mysql=MySQLConnector(app,'myownapi')


@app.route('/')
def index():
	query = "SELECT * FROM posts"
	posts = mysql.query_db(query)
	
	return render_template('index.html',posts=posts)


@app.route('/create',methods=['POST'])
def create():
	query = "INSERT INTO posts (description) VALUES('{}')".format(request.form['newpost'])
	mysql.query_db(query)

	return redirect('/')


@app.route('/create_json',methods=['GET', 'POST'])
def create_json():
	query = "INSERT INTO posts (description) VALUES('{}')".format(request.form['newpost'])
	mysql.query_db(query)

	query = "SELECT * FROM posts"
	posts = mysql.query_db(query)
	return jsonify(posts)


@app.route('/index_html',methods=['POST'])
def index_partial():
    query = "SELECT * FROM posts"
    posts = mysql.query_db(query)
    return render_template('posts.html', posts=posts)

app.run(debug=True)