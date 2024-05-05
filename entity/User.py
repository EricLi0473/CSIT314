import pymysql
from entity.Profile import Profile
class User:

    def __init__(self,userid = None,username = None,password = None,email = None,userTypeId = None,userStatus = None,userTypeName = None):
        self.userid = userid
        self.username = username
        self.password = password
        self.email = email
        self.userTypeId = userTypeId
        self.userStatus = userStatus
        self.userTypeName = userTypeName

    # 1.As a system admin, I want to be able to log into my account so that I can manage the system.
    # 12 As a real estate agent, I want to be able to log into my account so that I can access and manage various aspects of properties.
    # 21 As a seller, I want to be able to log into my account so that I can enter the real estate system.
    # 30 As a buyer, I want to be able to log into my account so that I can enter the real estate system.
    def checkLogin(self,username,password):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select password,userstatus from users where username = %s'
            cursor.execute(sqlQuery,username)
            value = cursor.fetchone()
            if value is None or value['UserStatus'] == 'invalid':
                return False
            realPassword = value['password']
            realStatus = value['userstatus']
            if realPassword == password and realStatus == 'valid':
                return True
            else:
                return False

    # 7 As a system admin, I want to be able to create a user account so that I can create an account to use.
    # 23 As a seller, I want to be able to create my account so that I can sell the property.
    # 32 As a buyer, I want to be able to create my account so that I can buy my interested properties.
    def addUser(self,username,password,email,userTypeId):
        values = (username,password,email,userTypeId,'valid')
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'insert into users (Username,Password,Email,UserTypeId,UserStatus) values (%s,%s,%s,%s,%s)'
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()
        return True

    # 8 As a system admin, I want to be able to read a user account so that I can view the details of accounts.
    def findAllUser(self):
        userList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from users left join profile on users.UserTypeId = profile.ProfileId;'
            cursor.execute(sqlQuery)
            userDataList = cursor.fetchall()
            for userData in userDataList:
                user = User(userData['UserId'],userData['Username'], userData['Password'], userData['Email'],userData['UserTypeId'],userData['UserStatus'],
                            userData['ProfileName'])
                userList.append(user)
        connect
        return userList

    # 9 As a system admin, I want to be able to update a user account so that I can update the user details of the account.
    # 25 As a seller, I want to be able to update my account so that I can ensure the details of information is correct.
    # 34 As a buyer, I want to be able to update my account so that I can keep my information new.
    def updateUser(self,oldUsername,newUsername,password,email,userTypeId):
        values = (newUsername,password,email,userTypeId,oldUsername)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'update users set Username = %s, Password = %s, Email = %s, UserTypeId = %s where Username = %s'
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()
        return True


    # 10 As a system admin, I want to be able to suspend user accounts so that I can stop the user’s access to the system if required.
    def suspendUser(self,username):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'update users set UserStatus = %s where Username = %s'
            cursor.execute(sqlQuery, ('invalid',username))
            connect.commit()
        connect.close()
        return True

    def activateUser(self,username):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'update users set UserStatus = %s where Username = %s'
            cursor.execute(sqlQuery, ('valid',username))
            connect.commit()
        connect.close()
        return True

    # 11 As a system admin, I want to be able to search a user account so that I can view the details of the accounts.
    # 24 As a seller, I want to be able to view my account so that I can ensure my details are correct.
    # 33 As a buyer, I want to be able to view my account so that I can ensure my details are correct.
    def findAUser(self, username):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        try:
            with connect.cursor() as cursor:
                sqlQuery = 'select * from users left join profile on users.UserTypeId = profile.ProfileId where username = %s'
                cursor.execute(sqlQuery, username)
                userData = cursor.fetchone()
                user = User(userData['UserId'],userData['Username'], userData['Password'], userData['Email'],userData['UserTypeId'],userData['UserStatus'],
                            userData['ProfileName'])
                return user
        except Exception:
            return User()
        finally:
            connect.close()

    def getAllAgentName(self):
        agentNameList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'select username from users where usertypeid = 2'
            cursor.execute(sqlQuery)
            agentNameData = cursor.fetchall()
            for agentName in agentNameData:
                agentNameList.append(agentName['username'])
        connect.close()
        return agentNameList
