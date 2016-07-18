from flask import Flask, render_template, redirect, request, jsonify
from mysqlconnection import MySQLConnector

app=Flask(__name__)
mysql=MySQLConnector(app,'myownapi')


############################################################
#index - this function is working
@app.route('/')
def index():
	query = "SELECT * FROM notes"
	notes = mysql.query_db(query)
	
	return render_template('index.html',notes=notes)

############################################################
#create - this function is working
@app.route('/create',methods=['POST'] )
def addNote():
	#SQL query here
	query="INSERT INTO notes (title,description) VALUES('{}','{}')".format(request.form['title'], request.form['description'])
	notes=mysql.query_db(query)
	# return notes
	return redirect('/')
############################################################


#create json
@app.route('/create_json',methods=['POST'])
def create():
	#SQL query here
	query="INSERT INTO notes (title,description) VALUES('{}','{}')".format(request.form['title'], request.form['description'])
	mysql.query_db(query)
	#get the id of new record
	query="SELECT id, title, description FROM notes ORDER BY id DESC LIMIT 1;"
	notes=mysql.query_db(query)
	return jsonify(notes)
	#return redirect('/')


############################################################
#update
@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
	#SQL to update specified record
	title=request.form['title']
	description=request.form['description']
	query="UPDATE notes SET title= :title, description= :description WHERE id= :id;"
	data = {
		'id': id,
		'title': title,
		'description': description
	}
	mysql.query_db(query,data)
	return redirect('/')

############################################################
#delete - this function is working
@app.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
	#SQL query to delete note
	query = "DELETE FROM notes WHERE id= :id;"
	data = {'id': id}
	#run query to delete record
	mysql.query_db(query,data)
	return redirect('/')

############################################################
app.run(debug=True)