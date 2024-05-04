from entity.Profile import Profile
class ViewProfilesController:
    def __init__(self):
        pass

    def viewAllProfile(self):
        return Profile().findAllProfile()

