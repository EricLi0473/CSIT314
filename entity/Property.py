import pymysql
from entity.NewFavorites import *
from entity.OldFavorits import *
class Property:

    def __init__(self,propertyId = None,title=None,description=None,bedNum=None,bathNum=None,size=None,price=None,status=None,
                 views=None,shortListed=None,agentId = None,sellerId = None,sellerName = None,agentName = None):
        self.propertyId = propertyId
        self.title = title
        self.description = description
        self.bedNum = bedNum
        self.bathNum = bathNum
        self.size = size
        self.price = price
        self.status = status
        self.views = views
        self.shortListed = shortListed
        self.agentId = agentId
        self.sellerId = sellerId
        self.sellerName = sellerName
        self.agentName = agentName

    # 14 As a real estate agent, I want to be able to create property listings so that I can show the property I am responsible for.
    def addProperty(self,title,description,bedNum,bathNum,size,price,agentid,sellerid):
        values = (title, description, bedNum, bathNum, size,price,'available','0','0',agentid,sellerid)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = ('insert into properties (Title,Description,BedNum,BathNum,Size,price,Status,Views,Shortlisted,AgentId,SellerId) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()
        return True

    # 15 As a real estate agent, I want to be able to view all properties in my account so that I can know what properties are in my property list.
    def findProperties(self,agentId):
        propertyList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'SELECT * FROM properties LEFT JOIN users AS Seller ON properties.SellerId = Seller.UserId LEFT JOIN users AS Agent ON properties.AgentId = Agent.UserId WHERE Agent.UserId = %s'
            cursor.execute(sqlQuery,agentId)
            propertyDataList = cursor.fetchall()
            for propertyData in propertyDataList:
                property = Property(propertyData['PropertyId'],propertyData['Title'], propertyData['Description'], propertyData['BedNum'],
                                    propertyData['BathNum'], propertyData['Size'], propertyData['Price'],
                                    propertyData['Status'], propertyData['Views'], propertyData['Shortlisted'],
                                    propertyData['AgentId'], propertyData['SellerId'], propertyData['Username'],propertyData['Agent.Username'])
                propertyList.append(property)
        connect.close()
        return propertyList

    # 16 As a real estate agent, I want to be able to update property listings so that I can ensure the details of the property are correct.
    def updateProperty(self,oldTitle,newTitle,description,bedNum,bathNum,size,price,status,
                       sellerId,views):
        values = (newTitle,description,bedNum,bathNum,size,price,status,views,sellerId,oldTitle)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'update properties set title = %s, description = %s, bedNum = %s, bathNum = %s ,size = %s, price = %s,status = %s,views = %s,SellerId = %s where title = %s'
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()
        return True

    # 17 As a real estate agent, I want to be able to remove property listings so that I can remove the unavailability property.
    def removeProperty(self, propertyId):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            if NewFavorites().FindNewFavouritesById(propertyId):
                sqlQuery = 'delete from newfavoriteslist where PropertyId = %s'
                cursor.execute(sqlQuery, propertyId)
            if OldFavorites().FindOldFavouritesById(propertyId):
                sqlQuery = 'delete from oldfavoriteslist where PropertyId = %s'
                cursor.execute(sqlQuery, propertyId)
            sqlQuery = 'delete from properties where PropertyId = %s'
            cursor.execute(sqlQuery, propertyId)
            connect.commit()
        connect.close()
        return True

    # 18 As a real estate agent, I want to be able to search property listings so that I can find the specific properties that I want to know.
    # 36 As a buyer, I want to be able to search both new and old property listings so that I can search the property with key words.
    def findAProperty(self, title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        try:
            with connect.cursor() as cursor:
                sqlQuery = 'SELECT * FROM properties LEFT JOIN users AS Seller ON properties.SellerId = Seller.UserId LEFT JOIN users AS Agent ON properties.AgentId = Agent.UserId where Title = %s'
                cursor.execute(sqlQuery, title)
                propertyData = cursor.fetchone()
                property = Property(propertyData['PropertyId'],propertyData['Title'], propertyData['Description'], propertyData['BedNum'],
                                    propertyData['BathNum'],propertyData['Size'],propertyData['Price'],
                                    propertyData['Status'],propertyData['Views'],propertyData['Shortlisted'],
                                    propertyData['AgentId'],propertyData['SellerId'],propertyData['Username'],propertyData['Agent.Username'])
                return property
        except Exception:
            return Property()
        finally:
            connect.close()

    # 35 As a buyer, I want to be able to view both new and old property listings so that I can view present property information.
    def viewAllProperty(self):
        propertyList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'SELECT * FROM properties LEFT JOIN users AS Seller ON properties.SellerId = Seller.UserId LEFT JOIN users AS Agent ON properties.AgentId = Agent.UserId'
            cursor.execute(sqlQuery)
            propertyDataList = cursor.fetchall()
            for propertyData in propertyDataList:
                property = Property(propertyData['PropertyId'],propertyData['Title'], propertyData['Description'], propertyData['BedNum'],
                                    propertyData['BathNum'], propertyData['Size'], propertyData['Price'],
                                    propertyData['Status'], propertyData['Views'], propertyData['Shortlisted'],
                                    propertyData['AgentId'], propertyData['SellerId'],propertyData['Username'],propertyData['Agent.Username'])
                propertyList.append(property)
        connect.close()
        return propertyList

    # 26 As a seller, I want to be able to view all my properties so that I can manage and track properties I own
    def findPropertyBySellerId(self,sellerId):
        propertyList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'SELECT * FROM properties LEFT JOIN users AS Seller ON properties.SellerId = Seller.UserId LEFT JOIN users AS Agent ON properties.AgentId = Agent.UserId where sellerId = %s'
            cursor.execute(sqlQuery,sellerId)
            propertyDataList = cursor.fetchall()
            for propertyData in propertyDataList:
                property = Property(propertyData['PropertyId'],propertyData['Title'], propertyData['Description'], propertyData['BedNum'],
                                    propertyData['BathNum'], propertyData['Size'], propertyData['Price'],
                                    propertyData['Status'], propertyData['Views'], propertyData['Shortlisted'],
                                    propertyData['AgentId'], propertyData['SellerId'],propertyData['Username'],propertyData['Agent.Username'])
                propertyList.append(property)
        connect.close()
        return propertyList

# print(Property().removeProperty(1))