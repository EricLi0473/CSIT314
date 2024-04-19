from entity.User import User
from entity.Review import Review

class GiveReviewToAgentControl:
    def __init__(self):
        pass

    def giveReviewToAgent(self,buyerName,agentName,rating,comment):
        buyerId = User().findUserIdByUserName(buyerName)
        agentId = User().findUserIdByUserName(agentName)
        return Review().addReview(buyerId,agentId,rating,comment)


