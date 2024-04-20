from entity.User import User
from entity.Property import Property

class UpdatePropertyControl:
    def __init__(self):
        pass
    def updatePropertry(self,newTitle,oldTitle,description,bedNum,bathNum,size,price,status,sellerName):
        try:
            sellerID = User().findUserIdByUserName(sellerName)
            Property().findAProperty(oldTitle)
            if not isinstance(bedNum, int) or not isinstance(bathNum, int) or not (isinstance(price, int) or isinstance(price, float)):
                raise Exception
            Property().updateProperty(newTitle=newTitle, oldTitle=oldTitle, description=description, bedNum=bedNum, bathNum=bathNum, size=size, price=price, status=status,sellerId=sellerID)
        except Exception:
            return False
        else:
            return True
'''
中介更新房产信息
更新成功返回True，如果错误返回False
'''

