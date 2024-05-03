import pymysql
class Comment:
    def __init__(self,commentId = None,senderId = None,receiverID = None,comment = None,senderName = None,receiverName = None):
        self.commentId = commentId
        self.senderId = senderId
        self.receiverId = receiverID
        self.comment = comment
        self.senderName = senderName
        self.receiverName = receiverName

    # 20 As a real estate agent, I want to be able to view my reviews of my services so that I can understand customer feedback and improve my service.
    def findCommentByAgentId(self, agentId):
        reviewsList = []
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = f'select * from comment left join users As Sender ON SenderId = Sender.UserId left join users As Receiver on ReceiverId = Receiver.UserId where receiverId = %s'
            cursor.execute(sqlQuery, agentId)
            reviewsDataList = cursor.fetchall()
            for review in reviewsDataList:
                review = Comment(review['CommentID'],review['SenderId'],review['ReceiverId'],review['Comment'],review['Username'],review['Receiver.Username'])
                reviewsList.append(review)
        connect.close()
        return reviewsList
    # 29 As a seller, I want to be able to write a text to review my experience working with a real estate agent so that other users can learn more.
    # 41 As a buyer, I want to be able to write a text to review my experience working with a real estate agent so that other users can learn more.
    def addComment(self,senderId,receiverId,comment):
        values = (senderId,receiverId,comment)
        connect = pymysql.connect(host='localhost', user='root', password='123456', database='db314',
                                  cursorclass=pymysql.cursors.DictCursor)
        with connect.cursor() as cursor:
            sqlQuery = 'insert into comment (SenderId,ReceiverId,Comment) values (%s,%s,%s)'
            cursor.execute(sqlQuery, values)
            connect.commit()
        connect.close()
        return True
