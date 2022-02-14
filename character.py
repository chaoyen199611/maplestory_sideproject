from logging import RootLogger
from account import Account

class Character(object):
    def __init__(self,name,role):
        self.name=name
        self.role=role
        self.income=0
