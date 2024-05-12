import pymysql
from entity.Property import *
class NewFavorites:

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


    # 37 As a buyer, I want to be able to save new property listings into favorite list so that I can manage and track properties I am interested in.
    def addIntoNewFavorities(self,buyerId,propertyId):
        values = (buyerId,propertyId)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = ('insert into newfavoriteslist (userid,propertyid) values (%s,%s)')
            cursor.execute(sqlQuery, values)
            connect.commit()
            sqlQuery = 'UPDATE properties SET shortlisted = shortlisted + 1 WHERE propertyId = %s'
            cursor.execute(sqlQuery, propertyId)
            connect.commit()
        connect.close()
        return True

    # 42 As a buyer, I want to be able to view my new property favorites list, so that I can track the property I'm interested in.
    def FindNewFavouritesByBuyer(self,buyerId):
        NewFavoritesList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select newfavoriteslist.UserId,newfavoriteslist.PropertyId,Title,Description,BedNum,BathNum,Size,Price,Status,Views,Shortlisted,Username as Agentname from newfavoriteslist left join properties on newfavoriteslist.PropertyId = properties.PropertyId left join users on AgentId = users.UserId where newfavoriteslist.UserId = %s'
            cursor.execute(sqlQuery, buyerId)
            NewFavoritesDataList = cursor.fetchall()
            for NewFavoriteData in NewFavoritesDataList:
                newFavorites = NewFavorites(NewFavoriteData['UserId'],NewFavoriteData['PropertyId'],NewFavoriteData['Title'],NewFavoriteData['Description'],
                                            NewFavoriteData['BedNum'],NewFavoriteData['BathNum'],NewFavoriteData['Size'],NewFavoriteData['Price'],
                                            NewFavoriteData['Status'],NewFavoriteData['Views'],NewFavoriteData['Shortlisted'],NewFavoriteData['Agentname'])
                NewFavoritesList.append(newFavorites)
        connect.close()
        return NewFavoritesList

    def FindNewFavouritesById(self,propertyId):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from newfavoriteslist where PropertyId = %s'
            cursor.execute(sqlQuery, propertyId)
            return cursor.fetchall()
