import pymysql
class Profile:
    def __init__(self, id = None, name = None):
        self.profileId = id
        self.profileName = name

    def getProfileId(self):
        return self.profileId

    def getProfileName(self):
        return self.profileName

    def findProfileNameById(self,profileId):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select profileName from profile where profileId = %s'
            cursor.execute(sqlQuery,profileId)
            name = cursor.fetchone()['profileName']
        connect.close()
        return name

    def findProfileIdByName(self,name):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select ProfileId from Profile where profileName = %s'
            cursor.execute(sqlQuery,name)
            profileId = cursor.fetchone()['ProfileId']
        connect.close()
        return profileId

    # 3 As a system admin, I want to be able to create a user profile so that I can create a profile for users.
    def addProfile(self,profileName):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'insert into profile (profilename) values (%s)'
            cursor.execute(sqlQuery,profileName)
            connect.commit()
        connect.close()
        return True

    # 4 As a system admin, I want to be able to read all user profile so that I can view the details of the profile.
    def findAllProfile(self):
        profileList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from profile'
            cursor.execute(sqlQuery)
            profileDataList = cursor.fetchall()
            for profileData in profileDataList:
                profile = Profile(profileData['ProfileId'],profileData['ProfileName'])
                profileList.append(profile)
        connect.close()
        return profileList

    # 5 As a system admin, I want to be able to update a user profile so that I can update the details of the profile.
    def updateProfile(self,oldProfileName, newProfileName):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'update profile set profileName = %s where profileName = %s'
            cursor.execute(sqlQuery,(oldProfileName,newProfileName))
            connect.commit()
        connect.close()
        return True

    # 6 As a system admin, I want to be able to search a user profile so that I can view the profile information for that user.
    def findAProfile(self,profileName):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from profile where profileName = %s'
            cursor.execute(sqlQuery,profileName)
            profileData = cursor.fetchone()
            profile = Profile(profileData['ProfileId'],profileData['ProfileName'])
        connect.close()
        return profile
