from flask import Flask
import random

app = Flask(__name__)

parts = [
    {'id': 1, 'title':'Back', 'body' : 'Back day'},
    {'id': 2, 'title':'Chest', 'body' : 'Chest day'},
    {'id': 3, 'title':'Leg', 'body' : 'Fucking Leg day'},
    {'id': 4, 'title':'Shoulder', 'body' : 'Plus Shoulder'},
    {'id': 5, 'title':'Bicepts/Tricepts', 'body' : 'Plus Arm'},
    {'id': 6, 'title':'Abs', 'body' : 'Plus Abs'}
]

@app.route('/')
def index():
    liTags = ''
    for part in parts:
        liTags += f'<li><a href="/read/{part["id"]}/">{part["title"]}</a></li>'
    return f'''<!doctype html>
    <html>
        <body>
                <h1><a href="/">WORKOUT</a></h1>
                <ol>
                    {liTags}
                </ol>
                <h2>Fighting !!</h2>
        </body>
    </html>    
    '''
    

@app.route('/read/<int:id>/')
def read(id):
    liTags = ''
    for part in parts:
        liTags += f'<li><a href="/read/{part["id"]}">{part["title"]}</a></li>'
    
    title = ''
    body = ''
    for part in parts:
        if id == part['id']:
            title = part['title']
            body = part['body']
            break
    
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WORKOUT</a></h1>
            <ol>
                {liTags}
            </ol>
            <h2>{title}</h2>
            {body}
        </body>
    </html>    
    '''

app.run(debug=True)