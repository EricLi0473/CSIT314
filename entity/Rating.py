import pymysql
class Rating:
    def __init__(self,ratingId = None,senderId = None,receiverID = None,rating = -1,senderName = None,receiverName = None):
        self.ratingId = ratingId
        self.senderId = senderId
        self.receiverId = receiverID
        self.rating = rating
        self.senderName = senderName
        self.receiverName = receiverName

    # 19 As a real estate agent, I want to be able to view my rating of my services so that I can understand customer feedback and improve my service.
    def findRatingByAgentId(self, agentId):
        reviewsList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from rating left join users As Sender ON SenderId = Sender.UserId left join users As Receiver on ReceiverId = Receiver.UserId where receiverId = %s'
            cursor.execute(sqlQuery, agentId)
            reviewsDataList = cursor.fetchall()
            for review in reviewsDataList:
                review = Rating(review['RatingID'],review['SenderId'],review['ReceiverId'],review['Rating'],review['Username'],review['Receiver.Username'])
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

