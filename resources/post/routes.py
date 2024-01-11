from flask import request
from uuid import uuid4 #unique identifier

from app import app
from db import posts, users

#post routes
@app.get('/post')
def get_posts():
    return{ 'posts': list(posts.values()) } #getting values not keys from above

@app.get('/post/<post_id>')
def get_post(post_id):
   try:
      return{'post': posts[post_id]}, 200
   except KeyError:
      return {'message': "Invalid Post"}, 400
   




@app.post('/post')
def create_post():
    #if a client creates a post they will send data here making social media post.
    post_data = request.get_json() #here they send data in json format
    print(post_data, '==========================================================\n\n')
    #posts[uuid4()] = post_data #What can go wrong is that 
    user_id = post_data['user_id']
    if user_id in users:
        posts[uuid4()] = post_data
        return { 'message': "Post Created"}, 201
    return {'message': "Invalid User"}, 401#           you can do just flask run, or manually do it in putting pp env.

#Above we are getting new user and not getting duplicates


@app.put('/post/<post_id>')
def update_post(post_id):
    try:
       post = post[post_id]
       post_data = request.get_json()
       if post_data['user_id']==post['user_id']:
          post['body'] = post_data['body']
          return {'message': 'Post Updated' }, 202
       return {'message': "Unauthorized"}, 401
    except:
       return {'message': "invalid Post Id"}, 400

@app.delete('/post/<post_id>')
def delete_post(post_id):
    try:
       del posts[post_id]
       return {'message': "Post deleted"}, 202
    except:
       return{'message':"Invalid Post"}, 400