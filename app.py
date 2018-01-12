from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://himanshu:piyush@ds046377.mlab.com:46377/todoapp')
db = client.todoapp

jinja_options = Flask.jinja_options.copy()
jinja_options.update(dict(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='%%',
    variable_end_string='%%',
    comment_start_string='<#',
    comment_end_string='#>',
))
app.jinja_options = jinja_options

@app.route("/")
def root():
   return render_template('index.html',data={ "name":"Piyush" })

@app.route("/api", methods = ['POST'])
def apiGateway(request):
	opcode 	= request.form.get('opcode')
	task 	= request.form.get('task')
	return jsonify( { "lol" : "lol"} )
	
if __name__ == "__main__":
    app.run(debug=True)