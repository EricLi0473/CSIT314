import pymysql
class Favorites:

    def __init__(self,userId = None, propertyId = None):
        self.userId = userId
        self.propertyId = propertyId

    def getUserId(self):
        return self.userId

    def getPropertyId(self):
        return self.propertyId

    # 37 As a buyer, I want to be able to save new property listings into favorite list so that I can manage and track properties I am interested in.
    # 38 As a buyer, I want to be able to save old property listings into favorite list so that I can manage and track properties I am interested in.
    def addIntoFavorities(self,buyerId,propertyId):
        values = (buyerId,propertyId)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = ('insert into buyerfavoriteslist (userid,propertyid) values (%s,%s)')
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()
        return True

