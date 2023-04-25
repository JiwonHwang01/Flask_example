from flask import Flask, request, redirect

app = Flask(__name__)
nextId = 7
parts = [
    {'id': 1, 'title':'Back', 'body' : 'Back day'},
    {'id': 2, 'title':'Chest', 'body' : 'Chest day'},
    {'id': 3, 'title':'Leg', 'body' : 'Fucking Leg day'},
    {'id': 4, 'title':'Shoulder', 'body' : 'Plus Shoulder'},
    {'id': 5, 'title':'Bicepts/Tricepts', 'body' : 'Plus Arm'},
    {'id': 6, 'title':'Abs', 'body' : 'Plus Abs'}
]

def templates(order, contents, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
            <li><form action="/delete/{id}/" method ="POST"><input type ="submit" value="delete"></form></li>
        '''
    return f'''<!doctype html>
    <html>
        <body>
                <h1><a href="/">WORKOUT</a></h1>
                <ol>
                    {order}
                </ol>
                {contents}
                <ul>
                    <li><a href="/create/">create</a></li>
                    {contextUI}
                </ul>
        </body>
    </html>    
    '''

def getOrder():
    liTags = ''
    for part in parts:
        liTags += f'<li><a href="/read/{part["id"]}/">{part["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    
    return templates(getOrder(), "<h2>Fighting !!</h2>")
    

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
    
    return templates(getOrder(), f'<h2>{title}</h2>{body}',id)

@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':

        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return templates(getOrder(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        parts.append(newTopic)
        url = '/read/'+ str(nextId) + '/'
        nextId += 1
        return redirect(url)
    
@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        title = ''
        body = ''
        for part in parts:
            if id == part['id']:
                title = part['title']
                body = part['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        return templates(getOrder(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']

        for part in parts:
            if id == part['id']:
                part['title'] = title
                part['body'] = body
                break
        url = '/read/'+ str(id) + '/' 
        return redirect(url)
    
@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    for part in parts:
        if id == part['id']:
            parts.remove(part)
            break
    return redirect('/')

app.run(debug=True)