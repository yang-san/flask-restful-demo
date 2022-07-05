from flask_restful import Resource, reqparse
from tools import min_length_str

userList = []

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'password', type=min_length_str(5), required=True,
        help= '{error_msg}'
    )

    def get(self, username):
        for user in userList:
            if user['username'] == username:
                return user
        return f'message: {username} 不存在',404

    def post(self, username):
        data = User.parser.parse_args()
        user = {
            'username':username,
            'password':data.get('password')
        }
        for u in userList:
            if u['username'] == username:
                return f'message: {username} 已存在',404
        userList.append(user)
        return f'message: {username} 已追加',201
    
    def put(self, username):
        data = User.parser.parse_args()
        for user in userList:
            if user['username'] == username:
                user['password'] = data.get('password')
                return f'message: {username} 修改完成',200

        return f'message: {username} not exists'

    def delete(self, username):
        for idx in range(len(userList)):
            if userList[idx]['username'] == username:
                del userList[idx]
                return f'message: {username} 移除成功', 201

        return f'message: 查無{username}, 移除失敗'
            

class UserList(Resource):
    def get(self):
        return userList

