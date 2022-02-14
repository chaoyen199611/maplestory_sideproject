from cgi import test
import random,string
from statistics import mode
from sqlalchemy import false, true
import pickle
import os

class Account(object):
    def create(self,account_name):
        self.account_name=account_name
        self.character=[]
        self.fileDir=""
        

    def load(self,account_name):
        pass

    def addCharacter(self,character):
        self.character.append(character)

    def loadall(self,filename):
        try:
            with open(self.fileDir+filename,"rb") as f:
                while True:
                    try:
                        yield pickle.load(f)
                    except EOFError:
                        break
        except:
            pass





        
""" 
if __name__=="__main__":
    a=Acount('chaoyen')
 """
