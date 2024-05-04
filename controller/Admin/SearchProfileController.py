from entity.Profile import Profile
class SearchProfileController:
    def __init__(self):
        pass
    def searchAProfile(self,name):
        return Profile().findAProfile(name)


print(SearchProfileController().searchAProfile("adm1in"))