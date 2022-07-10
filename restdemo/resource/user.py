from flask_restful import Resource, reqparse
from restdemo.tools import min_length_str

from restdemo import db
from restdemo.model import User as UserModel

userList = []

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'password', type=min_length_str(5), required=True,
        help= '{error_msg}'
    )

    def get(self, username):
        user = db.session.query(UserModel).filter(
            UserModel.username == username
        ).first()
        if user: 
            return user.as_dict()
        return f'message: 用戶 {username} 不存在',404

    def post(self, username):
        user = db.session.query(UserModel).filter(
            UserModel.username == username
        ).first()

        if not user:
            data = User.parser.parse_args()
            u = UserModel(
                username = username,
                password_hash = data.get('password'),
                email = data.get('email')
            )
            db.session.add(u)
            db.session.commit()
            return u.as_dict(), 201

        return f'message: {username} 已存在',404

    def put(self, username):
        data = User.parser.parse_args()
        user = db.session.query(UserModel).filter(
            UserModel.username == username
        ).first()
        if user:
            user.password_hash = data.get('password')
            db.session.commit()
            return f'message: {username} 修改完成',200

        return f'message: {username} not exists'

    def delete(self, username):
        user = db.session.query(UserModel).filter(
            UserModel.username == username
        ).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return f'message: {username} 移除成功', 201

        return f'message: 查無{username}, 移除失敗'


class UserList(Resource):
    def get(self):
        users = db.session.query(UserModel).all()
        return [u.as_dict() for u in users]
        

