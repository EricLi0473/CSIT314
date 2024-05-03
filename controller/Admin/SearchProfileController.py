from entity.Profile import Profile
class SearchProfileController:
    def __init__(self):
        pass
    def searchAProfile(self,name):
        return Profile().findAProfile(name)

    # def TransferProfileToList(self, profile):
    #     userText = []
    #     userText.append(profile.getProfileName())
    #     return userText
