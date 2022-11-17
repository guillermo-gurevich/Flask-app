class Config: 
#global settings
    SECRET_KEY = #Your Secret Key

class DevelopmentConfig(Config):
# setting for development env
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/test' #Name of DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = #Your gmail
    MAIL_PASSWORD = #You password

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/test_test' #Test DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'test': TestConfig
}