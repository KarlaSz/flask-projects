from flask import Flask

#steps
#install pip install flask and check interpreter
# set var env in terminal -> $env:FLASK_APP="main.py"
#check if exist var env -> echo $env:FLASK_APP
#flask run

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Nowy rok 2025!'




@app.route('/rok')
def year():
    #wielolinijkowy string w pythonie
    return '''
        <html>
        <head><title>Cześć nowy roku 2025!</title><head>
        <body>
            <h1>Cześć Tobie</h1>
            </body>
            </html>
    '''
#wykorzystac podane parametry w naszej app flask
@app.route('/hej/<name>')
def greeting(name):
    return f'Cześć {name}'

#parametr string lub id liczba np. z danymi id, z takim walidatorem od rauz
@app.route('/user/<int:id>')
def info_user(id):
    return f'Dane użytkownika o id: {id}'