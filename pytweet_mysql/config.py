"""FlaskのConfigを提供する"""
"""Provide Config of Flask"""
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    # EXERCISE: SQLAlchemyでMySQLを使うための設定を書こう 
      # EXERCISE: Make a setting for MySQL in SQLAlchemy ================
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': os.environ.get("MYSQL_USER") or "root",
        'password': os.environ.get("MYSQL_PASSWORD") or "password",
        'host': os.environ.get("DB_HOST") or "localhost",
        'db_name': os.environ.get("MYSQL_DATABASE") or "pytweet_mysql_development",
    })
    # =================================================================
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    

Config = DevelopmentConfig
