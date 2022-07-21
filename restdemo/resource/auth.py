
# 使用JWT功能 , 此段login 機能已可不用
'''
from flask_restful import Resource, reqparse
from restdemo.tools import min_length_str

from restdemo import db
from restdemo.model import User as UserModel


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'password', type=str, required=True,
        help= '{error_msg}'
    )

    parser.add_argument(
        'username', type=str, required=True,
        help= f'username required'
    )

    def post(self):
        data = Login.parser.parse_args()
        user = db.session.query(UserModel).filter(
            UserModel.username == data['username']
        ).first()
        if user:
            status = user.check_password(data['password']) # 判斷密碼是否正確
            if status:
                return {
                    'message': "login success",
                    'token': user.generate_token()
                }
            else:
                return f'login failed, please input the right username or password !  '

        return f'username not exists ! '

'''