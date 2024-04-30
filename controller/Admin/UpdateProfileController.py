from entity.Profile import Profile
class UpdateProfileController:
    def __init__(self):
        pass

    def updateProfile(self,oldUsername,newUsername):
        return Profile().updateProfile(oldUsername,newUsername)
