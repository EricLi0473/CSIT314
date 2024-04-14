import pymysql
class User:

    def __init__(self,userid = 0,username = 'username',password = 'password',email = 'email',userType = 'admin',userStatus = 'valid'):
        self.userid = userid
        self.username = username
        self.password = password
        self.email = email
        self.userType = userType
        self.userStatus = userStatus


    def getUserID(self):
        return self.userid
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getEmail(self):
        return self.email
    def getUserType(self):
        return self.userType
    def getUserStatus(self):
        return self.userStatus

    # add a new user into database. Error: pymysql.err.DataError
    def addUser(self,username,password,email,userType):
        values = (username,password,email,userType,'valid')
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        try:
            with connect.cursor() as cursor:
                sqlQuery = 'insert into users (Username,Password,Email,UserType,UserStatus) values (%s,%s,%s,%s,%s)'
                cursor.execute(sqlQuery, values)
                connect.commit()
        finally:
            connect.close()
        return True

    # update a user by username from database.
    def updataUser(self,oldUsername,newUsername,password,email,userType,userStatus):
        values = (newUsername,password,email,userType,userStatus,oldUsername)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        try:
            with connect.cursor() as cursor:
                sqlQuery = 'update users set Username = %s, Password = %s, Email = %s, UserType = %s ,UserStatus = %s where Username = %s'
                cursor.execute(sqlQuery, values)
                connect.commit()
        finally:
            connect.close()
        return True

    # search a user by username from database.
    def searchUser(self, username):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'select * from users where username = %s'
            cursor.execute(sqlQuery, username)
            userData = cursor.fetchone()
            if userData != None:
                user = User(userid= userData['UserId'],username= userData['Username'], password= userData['Password'],email= userData['Email'],userType= userData['UserType'],userStatus= userData['UserStatus'])
            else:
                raise Exception('Not found user')
        connect.close()
        return user

    # view all users.
    def findAllUser(self):
        userList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from users'
            cursor.execute(sqlQuery)
            userDataList = cursor.fetchall()
            for userData in userDataList:
                user = User(userData['UserId'],userData['Username'], userData['Password'], userData['Email'],userData['UserType'],userData['UserStatus'])
                userList.append(user)
        return userList

    def findUsernameByUserId(self,userId):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select username from users where userid = %s'
            cursor.execute(sqlQuery,userId)
            username = cursor.fetchone()['username']
        return username

    def findUserIdByUserName(self,username):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select userid from users where username = %s'
            cursor.execute(sqlQuery,username)
            userId = cursor.fetchone()['userid']
        return userId

    def findAllUserName(self):
        usernameList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select username from users'
            cursor.execute(sqlQuery)
            usernameDataList = cursor.fetchall()
            for usernameDate in usernameDataList:
                username = usernameDate['username']
                usernameList.append(username)
        return usernameList