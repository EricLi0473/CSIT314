from entity.User import User
from entity.Comment import Comment
from entity.Rating import Rating

class GiveCommentToAgentControl:
    def __init__(self):
        pass

    def giveCommentToAgent(self,senderId,agentName,comment):
        try:
            agentId = User().findAUser(agentName).userid
        except Exception:
            return False
        return Comment().addComment(senderId,agentId,comment)


