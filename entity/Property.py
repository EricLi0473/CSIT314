import pymysql
class Property:

    def __init__(self,title='title',description='description',bedNum='0',bathNum='0',size='0',price='0',status='available',
                 views='0',shortListed='0',agentId = '0',sellerId='0'):
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

    def setTitle(self, title):
        self.title = title
    def setDescription(self,description):
        self.description = description
    def setBedNum(self,bedNum):
        self.bedNum = bedNum
    def setBathNum(self,bathNum):
        self.bathNum = bathNum
    def setSize(self,size):
        self.size = size
    def setPrice(self,price):
        self.price = price
    def setStatus(self,status):
        self.status = status
    def setViews(self,views):
        self.views = views
    def setShortListed(self,shortListed):
        self.shortListed = shortListed
    def setAgentId(self,agentId):
        self.agentId = agentId
    def setSellName(self,sellerId):
        self.sellerId = sellerId

    def addProperty(self,title,description,bedNum,bathNum,size,price,agentid,sellerid):
        values = (title, description, bedNum, bathNum, size,price,'available','0','0',agentid,sellerid)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = ('insert into properties (Title,Description,BedNum,BathNum,Size,price,Status,Views,Shortlisted,AgentId,SellerId) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()

    def removeProperty(self, title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'delete from properties where title = %s'
            cursor.execute(sqlQuery, title)
            connect.commit()
        connect.close()

    def updateProperty(self,oldTitle,newTitle,description,bedNum,bathNum,size,price,status,
                       sellerId):
        values = (newTitle,description,bedNum,bathNum,size,price,status,sellerId,oldTitle)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        try:
            with connect.cursor() as cursor:
                sqlQuery = 'update properties set title = %s, description = %s, bedNum = %s, bathNum = %s ,size = %s, price = %s,status = %s,SellerId = %s where title = %s'
                cursor.execute(sqlQuery, values)
                connect.commit()
        finally:
            connect.close()
        return True

    def searchProperty(self, title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'select * from properties where title = %s'
            cursor.execute(sqlQuery, title)
            propertyData = cursor.fetchone()
            if propertyData != None:
                property = Property(propertyData['Title'], propertyData['Description'], propertyData['BedNum'],
                                    propertyData['BathNum'],propertyData['Size'],propertyData['Price'],
                                    propertyData['Status'],propertyData['Views'],propertyData['Shortlisted'],
                                    propertyData['AgentId'],propertyData['SellerId'])
            else:
                raise Exception('Not found property')
        connect.close()
        return property

    def findPropertyByAgentId(self,agentId):
        propertyList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from properties where agentId = %s'
            cursor.execute(sqlQuery,agentId)
            propertyDataList = cursor.fetchall()
            for propertyData in propertyDataList:
                property = Property(propertyData['Title'], propertyData['Description'], propertyData['BedNum'],
                                    propertyData['BathNum'], propertyData['Size'], propertyData['Price'],
                                    propertyData['Status'], propertyData['Views'], propertyData['Shortlisted'],
                                    propertyData['AgentId'], propertyData['SellerId'])
                propertyList.append(property)
        return propertyList

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
        return propertyList

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
        return propertyList

    def viewsCountPlasOne(self,title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select views from properties where title = %s'
            cursor.execute(sqlQuery, title)
            count = cursor.fetchone()['views']
            count = count + 1
            value = (count,title)
        with connect.cursor() as cursor:
            sqlQuery = 'update users set views = %s where title = %s'
            cursor.execute(sqlQuery, value)
        return True
    def findPropertyIdByName(self,title):
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select PropertyId from properties where Title = %s'
            cursor.execute(sqlQuery,title)
            propertyId = cursor.fetchone()['PropertyId']
        return propertyId

