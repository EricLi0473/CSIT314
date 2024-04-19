from entity.User import User
from entity.Property import Property
class CreatePropertyControl:
    def __init__(self):
        pass

    def createProperty(self,agentName,title, description, bedNum, bathNum, size, price,
                       Sellername):
        try:
            agentID = User().findUserIdByUserName(agentName)
            sellerID = User().findUserIdByUserName(Sellername)
        except Exception:
            return False
        return Property().addProperty(title=title,description=description,bedNum=bedNum,
                                       bathNum=bathNum,size=size,price=price,agentid=agentID,sellerid=sellerID)

'''
中介创建新的房产信息
创建成功返回True，错误返回False
'''
