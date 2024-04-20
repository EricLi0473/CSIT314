from entity.Profile import Profile
class ViewUserController:
    def __init__(self):
        pass

    def viewAllProfile(self):
        return Profile().findAllProfile()

    def TransferUserToList(self,profileList):
        profileTextList = []
        for profile in profileList:
            profileText = []
            profileText.append(profile.getProfileName())
            profileTextList.append(profileText)
        return profileTextList
