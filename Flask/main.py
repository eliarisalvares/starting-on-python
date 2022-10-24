from flask import Flask, request
from flask_restful import Api, Resource

# Overriding is an object-oriented programming feature that enables a child
# class to provide different implementation for a method that is already
# defined and/or implemented in its parent class or one of its parent classes.

app = Flask(__name__) # the value of "__name__" (dunder name) is used to locate
# the instance folder
# @seemore https://codefather.tech/blog/python-__name__-flask/
api = Api(app) # rest api

names = {"tim": {"age": 19, "gender": "male"},
       "bill": {"age": 56, "gender": "male"}}

class HelloWord(Resource):
   # make a class that is a resource holding different methods that can be
   # overrided to handle requests
   # defines what happens when a get request is sent to a determined url
   def get(self, name):
       # return {"Name": name} #key-value pair: every time something's returned
	   # from an API, it is important to make sure the information is
	   # serializable, inside a dictionary, f.e. - which is similar to json,so
	   # it can be serialized as such
       return names[name]
   def post(self):
       return {"Data": "Posted"}
#api.add_resource(HelloWord, "/helloworld")
api.add_resource(HelloWord, "/helloworld/<string:name>/") # use angle brackets
# to define parameter with type defined inside as well as the name of the
# parameter

# to run: python3 main.py
if __name__ == "__main__":
   app.run(debug=True) # start the server, flask app in debug mode, not to use
   # in production
