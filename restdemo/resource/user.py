from flask_restful import Resource, reqparse

userList = []

class User(Resource):
    
    def get(self, username):
        for user in userList:
            if user['username'] == username:
                return user
        return f'message: {username} 不存在',404

    def post(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'password', type=str, required=True,
            help='password required'
        )
        data = parser.parse_args()
        user = {
            'username':username,
            'password':data.get('password')
        }
        for u in userList:
            if u['username'] == username:
                return f'message: {username} 已存在',404
        userList.append(user)
        return f'message: {username} 已追加',201

class UserList(Resource):
    def get(self):
        return userList

