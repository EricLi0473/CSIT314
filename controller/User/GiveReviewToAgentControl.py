from entity.User import User
from entity.Comment import Comment
from entity.Rating import Rating

class GiveReviewToAgentControl:
    def __init__(self):
        pass

    def giveRatingToAgent(self,senderName,agentName,rating):
        try:
            senderId = User().findUserIdByUserName(senderName)
            agentId = User().findUserIdByUserName(agentName)
        except Exception:
            return False
        return Rating().addRating(senderId,agentId,rating)

    def giveCommentToAgent(self,senderName,agentName,comment):
        try:
            senderId = User().findUserIdByUserName(senderName)
            agentId = User().findUserIdByUserName(agentName)
        except Exception:
            return False
        return Comment().addComment(senderId,agentId,comment)


# g1 = GiveReviewToAgentControl()
# print(g1.giveRatingToAgent("seller1","agent1",1))
# print(g1.giveCommentToAgent("seller1","agent1","Not bad"))