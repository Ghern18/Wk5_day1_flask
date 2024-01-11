from flask import request
from uuid import uuid4

from app import app
from db import users

@app.get('/user') #route lets you run request by default!
def user():
    return {'users': list(users.values())}, 200

@app.get('/user/user_id>')
def get_user(user_id):
   try:
      return{ 'user': users[user_id]}
   except:
      return {'message': 'invalid user'}, 400
    

#post routes
@app.route ('/user', methods=["POST"]) #this or app.post either works :)
def create_user():
  user_data = request.get_json() #Here is where it come from flask to get the info. ()- is method. We take this data.
  for k in ['username', 'email', 'password']: #here we put in list
    if k not in user_data:
       return {'message': "Please include username email and password"}
  users[uuid4()] = user_data #here we pass in a unique identifyer
  return {'message': f'{user_data["username"]} created'}, 201 #Here we create a new user. Someone using a front end client they put input on here.
#How will we get the data? (eventually you can place so that there is no other user or password)

#below we are adding a url slugg - <> (here we looking for a specific user)
@app.put('/user/<user_id>') #how will flask know whar input we getting? We duplicate and change GET to POST in insomnia.
def update_user(user_id): #here we can update the data from whatever user they are using, new email etc.
    #if user_id in users: or another route.. below
    try:
      user = users[user_id]
      user_data = request.get_json()
      user |= user_data #short hand pipe == sign.   | = shift+\
      return {'message': f'{user["username"]}'}, 202
    except KeyError: #if there is any over lapping keys.
        return { 'message': "Invalid User"}, 400

        #if user['username'] == username: #here we have to consider 'hey we changin user or changing email?' bring in dynamic urls.

@app.delete('/user/<user_id>') #better order with slug
def delete_user(user_id):
    #user_data = request.get_json()
    #username = user_data['username']
  try:
    del users[user_id]
    return { 'message': f'User deleted'}, 202 #when we finish this for loop if we dont hit retunrn then invalid user.
  except:
    return {'messages': "Invalid username"}, 400
        #otherwise invalid user