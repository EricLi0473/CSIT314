import pymysql
class Review:
    def __init__(self,reviewId = 0,senderId = 0,receiverID = 0,rating = 5,comment = 'comment'):
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
        return reviewsList

