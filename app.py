from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
 
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
 
if __name__ == "__main__":
    app.run(debug=True)