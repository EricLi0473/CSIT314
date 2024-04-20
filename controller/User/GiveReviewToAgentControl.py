from entity.User import User
from entity.Review import Review

class GiveReviewToAgentControl:
    def __init__(self):
        pass

    def giveReviewToAgent(self,senderName,agentName,rating,comment):
        try:
            senderId = User().findUserIdByUserName(senderName)
            agentId = User().findUserIdByUserName(agentName)
        except Exception:
            return False
        return Review().addReview(senderId,agentId,rating,comment)

