from entity.User import User
from entity.Rating import Rating
class ViewRatingControl:
    def __init__(self):
        pass
    def viewRating(self,agentId):
        return Rating().findRatingByAgentId(agentId)
    '''
    查看中介名下所有！！！评分:int！！！,返回list[Reviews:object]
    [<entity.Review.Review object at 0x0000026355B3AD60>, <entity.Review.Review object at 0x0000026355B3ADC0>, <entity.Review.Review object at 0x0000026355B5D340>]
    '''



