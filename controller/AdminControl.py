from controller.UserControl import UserControl
from entity.Admin import Admin

class AdminControl(UserControl):

    def __init__(self,admin = Admin()):
        super().__init__(admin)

    '''
        admin create a new user in system
        Parameter: username:string, password:string, email:string, userType:string(admin, agent, buyer or seller)
        return createSuccess:bool
    '''
    def createUser(self,username,password,email,userType):
        usernameList = self.getUser().findAllUserName()
        if username in usernameList:
            raise Exception('Username have exist')
        else:
            self.getUser().addUser(username,password,email,userType)
            return True

    '''
        admin freeze a user in system
        Parameter: username:string
        return freezeSuccess:bool
    '''
    def freezeUser(self,username):
        try:
            user = self.getUser().searchUser(username)
            self.getUser().updataUser(user.getUsername(),user.getUsername(),
                                      user.getPassword(),user.getEmail(),user.getUserType(),'invalid')
            return True
        except Exception as e:
            return False


    def activateUser(self,username):
        try:
            user = self.getUser().searchUser(username)
            self.getUser().updataUser(user.getUsername(),user.getUsername(),
                                      user.getPassword(),user.getEmail(),user.getUserType(),'valid')
            return True
        except Exception as e:
            return False
    '''
        admin update a user in system
        Parameter: oldUsername:string,newUsername:string,password:string,email:string,userType:string(admin, agent, buyer or seller)
        return updateSuccess:bool
    '''
    def updateUser(self,oldUsername,newUsername,password,email,userType,states):
        usernameList = self.getUser().findAllUserName()
        usernameList.remove(oldUsername)
        if newUsername in usernameList:
            raise Exception('Username have exist')
        else:
            self.getUser().updataUser(oldUsername,newUsername,password,email,userType,states)


    '''
        admin find a new user in system by username
        Parameter: username:string
        return userText:double list
        [
            [username,password,email,usertype,state]
        ]
    '''
    def seachAUser(self,username):
        user = self.getUser().searchUser(username)
        userText = [[]]
        userText[0].append(user.getUsername())
        userText[0].append(user.getPassword())
        userText[0].append(user.getEmail())
        userText[0].append(user.getUserType())
        userText[0].append(user.getUserStatus())
        return userText

    '''
        admin view all user in system
        Parameter: None
        return userList:double list
        [
            [username,password,email,usertype,state],
            [username,password,email,usertype,state],
            ...
        ]
    '''
    def viewAllUser(self):
        userTextList = []
        userList = self.getUser().findAllUser()
        for user in userList:
            userText = []
            userText.append(user.getUsername())
            userText.append(user.getPassword())
            userText.append(user.getEmail())
            userText.append(user.getUserType())
            userText.append(user.getUserStatus())
            userTextList.append(userText)
        return userTextList
