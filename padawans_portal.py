
from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

users = {
  '1': {
    'username': 'dsmith',
    'email' : 'dsmith@ct.com',
  },
  '2' : {
    'username': "brandtc",
    'email': 'brandtc@ct.com',
  }
}

posts = {
  '1' : {
    'body' : 'FLASK WEEK LETS GO!!!',
    'user_id': '1'
  },
  '2': {
    'body': "Whiteboard was killer",
    'user_id': '2'
  },
  '3':{
    'body': 'SERVERS!!!!',
    'user_id' : '1'
  }
}

#CRUD Operations
#Create - POST
#Restreive - GET
#Update -put
#Delete

#user routes

@app.route('/user') #route lets you run request by default!
def user():
    return {'users': list(users.values())}, 200

@app.route ('/user', methods=["POST"])
def create_user():
    json_body = request.get_json()
    users[uuid4()] = json_body
    return {'message': f'{json_body["username"]} created'}, 201

@app.put('/user')
def update_users():
    return

@app.delete('/user')
def delete_user():
    pass

#post routes
@app.get('/post')
def get_posts():
    return

@app.post('/post')
def create_post():
    return

@app.put('/post')
def update_post():
    return

@app.delete('/post')
def delete_post():
    return

