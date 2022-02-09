from cgi import test
import random,string
from statistics import mode
from sqlalchemy import false, true

class Acount():
    def __init__(self,account_name):
        self.account_name=account_name
        self.account_id=self.generate_account_id()
        self.character=[]



    def generate_account_id(self):
        check=true
        with open("account/account_id.txt",mode='a+',encoding='utf-8') as file:
            while true:
                id=''.join(random.choice(string.ascii_uppercase+ string.digits) for x in range(10))
                for line in file:
                    if id == line:
                        check=false
                if check:
                    file.write(id)
                    file.write("\n")
                    break
        return id

    def get_account_id(self):
        return self.account_id


        

if __name__=="__main__":
    a=Acount('chaoyen')

