from entity.User import User
from entity.Property import Property

class RemovePropertyControl:
    def __init__(self):
        pass
    def remove_property(self,title):
        try:
            Property().findAProperty(title)
            Property().removeProperty(title)
        except Exception:
            return False
        else:
            return True
'''
中介删除房产
删除成功返回True，如果没找到房产title返回False
'''
