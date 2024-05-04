from entity.User import User
from entity.Comment import Comment
from entity.Rating import Rating

class GiveRatingToAgentControl:
    def __init__(self):
        pass

    def giveRatingToAgent(self,senderId,agentName,rating):
        try:
            agentId = User().findAUser(agentName).userid
        except Exception:
            return False
        return Rating().addRating(senderId,agentId,rating)

