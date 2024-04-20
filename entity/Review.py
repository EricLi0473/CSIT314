import pymysql
class Review:
    def __init__(self,reviewId = None,senderId = None,receiverID = None,rating = None,comment = None):
        self.reviewId = reviewId
        self.senderId = senderId
        self.receiverId = receiverID
        self.rating = rating
        self.comment = comment

    def getReviewId(self):
        return self.reviewId

    def getSenderId(self):
        return self.senderId

    def getReceiverId(self):
        return self.receiverId

    def getRating(self):
        return self.rating

    def getComment(self):
        return self.comment

    # 19 As a real estate agent, I want to be able to view my rating of my services so that I can understand customer feedback and improve my service.
    # 20 As a real estate agent, I want to be able to view my reviews of my services so that I can understand customer feedback and improve my service.
    def findReviewByAgentId(self, agentId):
        reviewsList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from reviews where receiverId = %s'
            cursor.execute(sqlQuery, agentId)
            reviewsDataList = cursor.fetchall()
            for review in reviewsDataList:
                review = Review(review['ReviewID'],review['SenderId'],review['ReceiverId'],review['Rating'],review['Comment'])
                reviewsList.append(review)
        connect.close()
        return reviewsList

    # 28 As a seller, I want to be able to submit a rating in the system for the real estate agents so that I can share my satisfaction and experience.
    # 29 As a seller, I want to be able to write a text to review my experience working with a real estate agent so that other users can learn more.
    # 40 As a buyer, I want to be able to submit a rating in the system for the real estate agents so that I can share my satisfaction and experience.
    # 41 As a buyer, I want to be able to write a text to review my experience working with a real estate agent so that other users can learn more.
    def addReview(self,senderId,receiverId,rating,comment):
        values = (senderId,receiverId,rating,comment)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'insert into reviews (SenderId,ReceiverId,Rating,Comment) values (%s,%s,%s,%s)'
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()
        return True