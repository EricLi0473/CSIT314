from entity.Profile import Profile

class CreateProfileController:
    def __init__(self):
        pass

    def createProfile(self,name):
        return Profile().addProfile(name)



"全新的用户类型"