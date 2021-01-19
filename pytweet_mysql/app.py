# flask appの初期化を行い、flask appオブジェクトの実体を持つ | Initialize flask app and get an instance of flask app object 
from flask import Flask
from pytweet_mysql.database import init_db
import pytweet_mysql.models


def create_app():
    # インスタンスの立ち上げ | Start up instance application
    _app = Flask(__name__)
    # Flaskのconfigが 設定ファイルを読み込む処理 | Import settings for config of Flask
    _app.config.from_object('pytweet_mysql.config.Config')
    # Secret Keyの設定 | Configure secret key to create secure session of DB
    _app.secret_key = 'hogehoge'

    # DBの初期化 | Initialize DB
    init_db(_app)

    return _app


app = create_app()
