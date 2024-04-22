import pymysql
class Rating:
    def __init__(self,ratingId = None,senderId = None,receiverID = None,rating = -1):
        self.ratingId = ratingId
        self.senderId = senderId
        self.receiverId = receiverID
        self.rating = rating
    def getRatingId(self):
        return self.ratingId

    def getSenderId(self):
        return self.senderId

    def getReceiverId(self):
        return self.receiverId

    def getRating(self):
        return self.rating

    # 19 As a real estate agent, I want to be able to view my rating of my services so that I can understand customer feedback and improve my service.
    def findRatingByAgentId(self, agentId):
        reviewsList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from rating where receiverId = %s'
            cursor.execute(sqlQuery, agentId)
            reviewsDataList = cursor.fetchall()
            for review in reviewsDataList:
                review = Rating(review['RatingID'],review['SenderId'],review['ReceiverId'],review['Rating'])
                reviewsList.append(review)
        connect.close()
        return reviewsList

    # 28 As a seller, I want to be able to submit a rating in the system for the real estate agents so that I can share my satisfaction and experience.
    # 40 As a buyer, I want to be able to submit a rating in the system for the real estate agents so that I can share my satisfaction and experience.
    def addRating(self,senderId,receiverId,rating):
        values = (senderId,receiverId,rating)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'insert into rating (SenderId,ReceiverId,Rating) values (%s,%s,%s)'
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()
        return True
