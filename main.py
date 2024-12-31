from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#START steps
#install pip install flask and check interpreter
# set var env in terminal -> $env:FLASK_APP="main.py"
#check if exist var env -> echo $env:FLASK_APP
#flask run

app = Flask(__name__)
#into configuration my app have to let know where my db is located, engine sqlite - only file name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

#object to interactions
db = SQLAlchemy(main)

#class which represent table
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)



#start app
@app.route('/', methods=['GET', 'POST'])
def todo():
    tasks = []
    if request.method == 'POST':
        tasks.append(request.form['task'])
    return render_template('todo.html', tasks=tasks)