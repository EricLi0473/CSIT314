import pymysql
class NewFavorites:

    def __init__(self,userId = None, propertyId = None):
        self.userId = userId
        self.propertyId = propertyId

    def getUserId(self):
        return self.userId

    def getPropertyId(self):
        return self.propertyId

    # 37 As a buyer, I want to be able to save new property listings into favorite list so that I can manage and track properties I am interested in.
    def addIntoNewFavorities(self,buyerId,propertyId):
        values = (buyerId,propertyId)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = ('insert into newfavoriteslist (userid,propertyid) values (%s,%s)')
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()
        return True

    # 42 As a buyer, I want to be able to view my new property favorites list, so that I can track the property I'm interested in.
    def FindNewFavouritesByBuyer(self,buyerId):
        NewFavoritesList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select userid,propertyid from NewFavoritesList where userid = %s'
            cursor.execute(sqlQuery, buyerId)
            NewFavoritesDataList = cursor.fetchall()
            for NewFavoriteData in NewFavoritesDataList:
                newFavorites = NewFavorites(NewFavoriteData['userid'],NewFavoriteData['propertyid'])
                NewFavoritesList.append(newFavorites)
        connect.close()
        return NewFavoritesList

