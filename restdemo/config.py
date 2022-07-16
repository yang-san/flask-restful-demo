'''
配置文件
'''
from datetime import timedelta
class DB_settings:
    def __init__(self):
        DB_TYPE = "mysql"
        DB_DRIVER = "pymysql"
        DB_USERNAME = "root"
        DB_PASSWORD = "root"
        DB_HOST = "localhost"
        DB_PORT = "3306"
        DB_NAME = "flask_demo"

        #DB_URL = "sqlite:///demo.db"
        self.DB_URL = f"{DB_TYPE}+{DB_DRIVER}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    def get_db(self):
        return self.DB_URL


class Config:
    SQLALCHEMY_DATABASE_URI = DB_settings().get_db()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'flask999'
    JWT_EXPIRATION_DELTA = timedelta(seconds=300) #5分鐘延遲