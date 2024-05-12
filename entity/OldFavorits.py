import pymysql
class OldFavorites:

    def __init__(self,userId = None, propertyId = None,Title = None,Description = None,BedNum = None,BathNum = None,Size = None,Price = None,Status = None,
                 Views = None,Shortlisted = None,Agentname = None):
        self.userId = userId
        self.propertyId = propertyId
        self.Title = Title
        self.Description = Description
        self.BedNum = BedNum
        self.BathNum = BathNum
        self.Size = Size
        self.Price = Price
        self.Status = Status
        self.Views = Views
        self.Shortlisted = Shortlisted
        self.Agentname = Agentname

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
            sqlQuery = f'select oldfavoriteslist.UserId,oldfavoriteslist.PropertyId,Title,Description,BedNum,BathNum,Size,Price,Status,Views,Shortlisted,Username as Agentname from oldfavoriteslist left join properties on oldfavoriteslist.PropertyId = properties.PropertyId left join users on AgentId = users.UserId where oldfavoriteslist.UserId = %s'
            cursor.execute(sqlQuery, buyerId)
            OldFavoritesDataList = cursor.fetchall()
            for OldFavoriteData in OldFavoritesDataList:
                oldFavorites = OldFavorites(OldFavoriteData['UserId'],OldFavoriteData['PropertyId'],OldFavoriteData['Title'],
                                            OldFavoriteData['Description'],OldFavoriteData['BedNum'],OldFavoriteData['BathNum'],
                                            OldFavoriteData['Size'],OldFavoriteData['Price'],OldFavoriteData['Status'],OldFavoriteData['Views'],
                                            OldFavoriteData['Shortlisted'],OldFavoriteData['Agentname'])
                OldFavoritesList.append(oldFavorites)
        connect.close()
        return OldFavoritesList

    def FindOldFavouritesById(self,propertyId):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from oldfavoriteslist where PropertyId = %s'
            cursor.execute(sqlQuery, propertyId)
            return cursor.fetchall()
