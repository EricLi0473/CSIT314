from entity.User import User
from entity.Comment import Comment
class ViewCommentControl:
    def __init__(self):
        pass
    def viewComment(self,agentId):
        return Comment().findCommentByAgentId(agentId)
    '''
    查看中介名下所有！！！评论:string！！！,返回list[Reviews:object]
    [<entity.Review.Review object at 0x0000026355B3AD60>, <entity.Review.Review object at 0x0000026355B3ADC0>, <entity.Review.Review object at 0x0000026355B5D340>]
    '''
