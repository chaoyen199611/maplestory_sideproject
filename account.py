from cgi import test
import random,string
from statistics import mode
from sqlalchemy import false, true

class Account(object):
    def __init__(self,account_name):
        self.account_name=account_name
        self.character=[]

    def load(self,account_name):
        pass

    def addCharacter(self,character):
        self.character.append(character)





        
""" 
if __name__=="__main__":
    a=Acount('chaoyen')
 """
