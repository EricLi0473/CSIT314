from entity.Property import Property
from entity.User import User

class ViewPropertiesController:
    def __init__(self):
        pass

    def viewProperties(self):
        return Property().viewAllProperty()

