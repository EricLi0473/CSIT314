import pymysql
class Favorites:

    def __init__(self,userId = 0, propertyId = 0):
        self.userId = userId
        self.propertyId = propertyId

    def getUserId(self):
        return self.userId

    def getPropertyId(self):
        return self.propertyId

    def addIntoFavorities(self,buyerId,propertyId):
        try:
            values = (buyerId,propertyId)
            connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                      cursorclass=pymysql.cursors.DictCursor)
            with connect.cursor() as cursor:
                sqlQuery = ('insert into buyerfavoriteslist (userid,propertyid) values (%s,%s)')
                cursor.execute(sqlQuery, values)
                connect.commit()
                return True
        except Exception:
            return False
        finally:
            connect.close()

