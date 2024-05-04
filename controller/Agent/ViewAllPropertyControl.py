from entity.User import User
from entity.Property import Property
class ViewAllPropertyControl:
    def __init__(self):
        pass
    def viewAllProperties(self,agentId):
        return Property().findProperties(agentId)

    '''
    查看中介名下所有房产,返回list[Property:object]
    [<entity.Property.Property object at 0x0000021151D759A0>, <entity.Property.Property object at 0x0000021151D75970>,]
    '''

