import os


class Config:
    DATABASE = "IPL"
    USERNAME = os.environ.get('DB_USERNAME')
    PWD = os.environ.get('PWD')
    HOST = os.environ.get('DB_HOSTNAME')
