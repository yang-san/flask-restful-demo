from flask import Flask
from flask_restful import Resource, Api

from resource.user import User, UserList
from resource.hello import Helloworld

app = Flask(__name__)
api = Api(app)

api.add_resource(Helloworld, '/')
api.add_resource(User, '/user/<username>')
api.add_resource(UserList, '/users')

if __name__ == "__main__":
    app.run()