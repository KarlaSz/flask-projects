from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "todo.db")}'
db = SQLAlchemy(app)

#object aplication to interactions
#model, class which represent table
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

#start app, get and show items
@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task_name = request.form['task']
        if task_name.strip():  # check if task is not empty
            task = Task(name=task_name)
            db.session.add(task)
            db.session.commit()
        return redirect(url_for('todo')) #redirect to home page

    tasks = Task.query.all()
    return render_template('todo.html', tasks=tasks)

#delete item
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('todo'))

#edit item
@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        task.name = request.form['task']  # change item name
        db.session.commit()
        return redirect(url_for('todo'))  # after saving back to home page

    return render_template('edit_task.html', task=task)
