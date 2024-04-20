import pymysql
class Property:

    def __init__(self,title=None,description=None,bedNum=None,bathNum=None,size=None,price=None,status=None,
                 views=None,shortListed=None,agentId = None,sellerId = None):
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

    def getTitle(self):
        return self.title
    def getDescription(self):
        return self.description
    def getBedNum(self):
        return  self.bedNum
    def getBathNum(self):
        return  self.bathNum
    def getSize(self):
        return self.size
    def getPrice(self):
        return  self.price
    def getStatus(self):
        return self.status
    def getViews(self):
        return self.views
    def getShortListed(self):
        return self.shortListed
    def getAgentId(self):
        return self.agentId
    def getSellerId(self):
        return self.sellerId

    def findPropertyIdByTitle(self,title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select PropertyId from properties where Title = %s'
            cursor.execute(sqlQuery,title)
            propertyId = cursor.fetchone()['PropertyId']
        connect.close()
        return propertyId

    def findPropertyTitledById(self, propertyId):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select Title from properties where PropertyId= %s'
            cursor.execute(sqlQuery, propertyId)
            propertyTitle = cursor.fetchone()['Title']
        connect.close()
        return propertyTitle

    def viewsCountPlasOne(self, title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select views from properties where title = %s'
            cursor.execute(sqlQuery, title)
            count = cursor.fetchone()['views']
            count = count + 1
            value = (count, title)
            sqlQuery = 'update properties set views = %s where title = %s'
            cursor.execute(sqlQuery, value)
            connect.commit()
        connect.close()
        return True

    def favoritesCountPlasOne(self, title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select shortlisted from properties where title = %s'
            cursor.execute(sqlQuery, title)
            count = cursor.fetchone()['shortlisted']
            count = count + 1
            value = (count, title)
            sqlQuery = 'update properties set shortlisted = %s where title = %s'
            cursor.execute(sqlQuery, value)
            connect.commit()
        connect.close()
        return True

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
    def findPropertyByAgentId(self,agentId):
        propertyList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from properties where agentId = %s'
            cursor.execute(sqlQuery,agentId)
            propertyDataList = cursor.fetchall()
            if propertyDataList is None:
                return Property()
            for propertyData in propertyDataList:
                property = Property(propertyData['Title'], propertyData['Description'], propertyData['BedNum'],
                                    propertyData['BathNum'], propertyData['Size'], propertyData['Price'],
                                    propertyData['Status'], propertyData['Views'], propertyData['Shortlisted'],
                                    propertyData['AgentId'], propertyData['SellerId'])
                propertyList.append(property)
        connect.close()
        return propertyList

    # 16 As a real estate agent, I want to be able to update property listings so that I can ensure the details of the property are correct.
    def updateProperty(self,oldTitle,newTitle,description,bedNum,bathNum,size,price,status,
                       sellerId):
        values = (newTitle,description,bedNum,bathNum,size,price,status,sellerId,oldTitle)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'update properties set title = %s, description = %s, bedNum = %s, bathNum = %s ,size = %s, price = %s,status = %s,SellerId = %s where title = %s'
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()
        return

    # 17 As a real estate agent, I want to be able to remove property listings so that I can remove the unavailability property.
    def removeProperty(self, title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'delete from properties where title = %s'
            cursor.execute(sqlQuery, title)
            connect.commit()
        connect.close()
        return True

    # 18 As a real estate agent, I want to be able to search property listings so that I can find the specific properties that I want to know.
    # 36 As a buyer, I want to be able to search both new and old property listings so that I can search the property with key words.
    def findAProperty(self, title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'select * from properties where title = %s'
            cursor.execute(sqlQuery, title)
            propertyData = cursor.fetchone()
            if propertyData is None:
                return Property()
            property = Property(propertyData['Title'], propertyData['Description'], propertyData['BedNum'],
                                propertyData['BathNum'],propertyData['Size'],propertyData['Price'],
                                propertyData['Status'],propertyData['Views'],propertyData['Shortlisted'],
                                propertyData['AgentId'],propertyData['SellerId'])
        connect.close()
        return property

    # 26 As a seller, I want to be able to track the number of views on properties so that I can know how many people are interested in this property.
    def findViewByTitle(self, title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'select views from properties where title = %s'
            cursor.execute(sqlQuery, title)
            view = cursor.fetchone()['views']
        connect.close()
        return view

    # 27 As a seller, I want to be able to track the number of times being shortlisted on properties so that I can better understand the market feedback and demand for property.
    def findShortlistedByTitle(self, title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'select views from properties where title = %s'
            cursor.execute(sqlQuery, title)
            shortlisted = cursor.fetchone()['Shortlisted']
        connect.close()
        return shortlisted

    # 35 As a buyer, I want to be able to view both new and old property listings so that I can view present property information.
    def viewAllProperty(self):
        propertyList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from properties'
            cursor.execute(sqlQuery)
            propertyDataList = cursor.fetchall()
            for propertyData in propertyDataList:
                property = Property(propertyData['Title'], propertyData['Description'], propertyData['BedNum'],
                                    propertyData['BathNum'], propertyData['Size'], propertyData['Price'],
                                    propertyData['Status'], propertyData['Views'], propertyData['Shortlisted'],
                                    propertyData['AgentId'], propertyData['SellerId'])
                propertyList.append(property)
        connect.close()
        return propertyList

    # 39 As a buyer, I want to be able to calculate the monthly payments based on the price of the property, interest rate, and other relevant factors so that I can know if the property is within my budget.
    def calculateMonthlyPayments(self,title,month):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select price from properties where title = %s'
            cursor.execute(sqlQuery,title)
            price = cursor.fetchone()['Price']
        connect.close()
        return  price/month

    # 42 As a seller, I want to be able to view all my properties so that I can manage and track properties I own
    def findPropertyBySellerId(self,sellerId):
        propertyList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from properties where sellerId = %s'
            cursor.execute(sqlQuery,sellerId)
            propertyDataList = cursor.fetchall()
            for propertyData in propertyDataList:
                property = Property(propertyData['Title'], propertyData['Description'], propertyData['BedNum'],
                                    propertyData['BathNum'], propertyData['Size'], propertyData['Price'],
                                    propertyData['Status'], propertyData['Views'], propertyData['Shortlisted'],
                                    propertyData['AgentId'], propertyData['SellerId'])
                propertyList.append(property)
        connect.close()
        return propertyList

