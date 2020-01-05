import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    IS_AZUR_DEPLOYMENT = True

    if IS_AZUR_DEPLOYMENT :
        dbuser = "admindb@dbazur"
        dbpass = "0aDB2020"
        dbhost = "dbazur.postgres.database.azure.com"
        dbname = "dbazur"
        
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
            dbuser,dbpass,dbhost, dbname)
    else :
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
            dbuser=os.environ['DBUSER'],
            dbpass=os.environ['DBPASS'],
            dbhost=os.environ['DBHOST'],
            dbname=os.environ['DBNAME'])
    
class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
