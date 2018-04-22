''' Configuration file '''

class Database:
    DB = 'communityDB'
    HOST = 'communitydbinstance.ci19co3on1ki.us-east-2.rds.amazonaws.com'
    PORT = 3306
    USER = 'Pablodb'
    PAS  = '|H0rizon3.14X|'



class App:
    API_VERSION = 1
    URL_PREFIX = '/api/v' + str(API_VERSION)
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = 8000
