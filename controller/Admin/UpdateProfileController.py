from entity.Profile import Profile
class UpdateProfileController:
    def __init__(self):
        pass

    def updateProfile(self,oldUsername,newUsername):
        return Profile().updateProfile(oldUsername,newUsername)

a = UpdateProfileController().updateProfile('Master','XXX')
print(a)