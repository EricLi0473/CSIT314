from entity.User import User
from entity.Property import Property


class SearchPropertyControl:
    def __init__(self):
        pass

    def searchProperty(self, title):
        property = Property().findAProperty(title)
        return property

    '''
    中介按照title搜索房产
    搜索成功返回Property:object，不成功返回 空的 Property:object,
    '''


