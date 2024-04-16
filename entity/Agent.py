import pymysql
from entity.User import User
class Agent(User):
    def __init__(self,userid = 0,username = 'username',password = 'password',email = 'email',userStatus = 'valid',properties = []):
        super().__init__(userid= userid,username = username,password = password,email = email,userType='agent',userStatus = userStatus)
        self.properties = properties

    def getProperties(self):
        return self.properties

    def setProperties(self,properties):
        self.properties = properties
