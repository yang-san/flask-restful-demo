from hashlib import algorithms_available
from xmlrpc.client import Boolean
from restdemo import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask import current_app
import jwt

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique = True)

    def __repr__(self):
        return f'id={self.id}, username={self.username}'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        return self.password_hash
    
    def check_password(self, password)->Boolean:
        return check_password_hash(self.password_hash, password)

    def generate_token(self):
        ''' Token生成 '''
        try:
            # 設定payload跟Token的有效時間
            payload = {
                'exp':datetime.utcnow() + timedelta(minutes=5), # Token有效時間
                'iat':datetime.utcnow(), # 有效時間的計算基準
                'sub':self.username # 認證方式
            }
            # 產生Token (使用Payload / 加密鑰匙)
            jwt_token = jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'), #加密鑰匙
                algorithm="HS256" # 使用的演算法
            )
            return jwt_token.decode()

        except Exception as ex:
            return str(ex)

    @staticmethod
    def authenticate(username, password):
        # 驗證用戶名
        user = db.session.query(User).filter(
            User.username == username
        ).first()
        if user:
            if user.check_password(password):
                return user

    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        user = db.session.query(User).filter(
            User.id == user_id
        )
        return user