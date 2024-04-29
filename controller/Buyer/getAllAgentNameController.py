from entity.User import User

class getAllAgentNameController:
    def __init__(self):
        pass

    def getAllAgentName(self):
        return User().getAllAgentName()

# ['agent1', 'agent2']