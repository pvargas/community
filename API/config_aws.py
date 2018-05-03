''' Configuration file '''

class Database:
    DB = 'communityDB'
    HOST = 'communitydbinstance.ci19co3on1ki.us-east-2.rds.amazonaws.com'
    PORT = 3306
    USER = 'Pablodb'
    PAS  = '|H0rizon3.14X|'



class App:
    API_VERSION = 1
    #URL_PREFIX = '/api/v' + str(API_VERSION)
    URL_PREFIX = ''
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 8000
    SECRET = '4Q*hrG3EMG@r^!oMBlQ1Z3PmQLbs@WR*^74j#7BCWAaX9J3$lFzHxLUnkmo'