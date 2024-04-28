from entity.Property import Property
class TrackPropertyShortlistedController:
    def __init__(self):
        pass
    def trackPropertyViewed(self,title):
        return Property().findShortlistedByTitle(title)


