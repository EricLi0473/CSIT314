from entity.Profile import Profile
class ViewProfilesController:
    def __init__(self):
        pass

    def viewAllProfile(self):
        return Profile().findAllProfile()

    # def TransferProfileToList(self,profileList):
    #     profileTextList = []
    #     for profile in profileList:
    #         profileText = []
    #         profileText.append(profile.getProfileName())
    #         profileTextList.append(profileText)
    #     return profileTextList
