import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', None)
    if SECRET_KEY is None:
        print("SECRET_KEY should not be done!")


class DevConfig(Config):
    ENV = 'DEV'
    DEBUG = True


class ProdConfig(Config):
    ENV = 'PROD'
    DEBUG = False
