from entity.User import User

class Admin(User):
    def __init__(self,username = 'username',password = 'password',email = 'email',userStatus = 'valid'):
        super().__init__(username = username,password = password,email = email,userType='admin',userStatus = userStatus)


