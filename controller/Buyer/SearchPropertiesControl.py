from entity.Property import Property
from entity.User import User
class SearchPropertiesControl:
    def __init__(self):
        pass
    def SearchProperty(self,title):
        property = Property().searchProperty(title)
        propertyText = []
        propertyText.append(property.getTitle())
        propertyText.append(property.getDescription())
        propertyText.append(property.getBedNum())
        propertyText.append(property.getBathNum())
        propertyText.append(property.getSize())
        propertyText.append(property.getPrice())
        propertyText.append(property.getStatus())
        Property().viewsCountPlasOne(title)
        return propertyText

'''
用法：按照title搜索房产信息
返回值：一维列表
['Property1', 'Beautiful house with a garden', 3, 2, 2000, 300000.0, 'available']
'''

