import pymysql
class OldFavorites:

    def __init__(self,userId = None, propertyId = None):
        self.userId = userId
        self.propertyId = propertyId

    def getUserId(self):
        return self.userId

    def getPropertyId(self):
        return self.propertyId

    # 38 As a buyer, I want to be able to save old property listings into favorite list so that I can manage and track properties I am interested in.
    def addIntoOldFavorities(self,buyerId,propertyId):
        values = (buyerId,propertyId)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = ('insert into oldfavoriteslist (userid,propertyid) values (%s,%s)')
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()
        return True

    # 43 As a buyer, I want to be able to view my old property favorites list, so that I can track the property I'm interested in.
    def FindOldFavouritesByBuyer(self,buyerId):
        OldFavoritesList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select userid,propertyid from OldFavoritesList where userid = %s'
            cursor.execute(sqlQuery, buyerId)
            OldFavoritesDataList = cursor.fetchall()
            for OldFavoriteData in OldFavoritesDataList:
                oldFavorites = OldFavorites(OldFavoriteData['userid'],OldFavoriteData['propertyid'])
                OldFavoritesList.append(oldFavorites)
        connect.close()
        return OldFavoritesList