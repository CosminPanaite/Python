class FootballTeam:
    def __init__(self,name,players,value):
        self.__name=name
        self.__players=players
        self.__value=value
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name=new_name

    def get_value(self):
        return self.__players


    def set_players(self, new_players):
        self.__players=new_players

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value=new_value

    def __repr__(self):
        return "Team " + str(self.__name) + " with the number of " + str(self.__players) + " players "  + "with the value "  +str(self.__value)
    def get_all_teams(self,team:FootballTeam):
        self.__teams=[]
        self.__teams.append(team)
        return self.__teams

Che=FootballTeam("Chelsea",31,850)
Rma=FootballTeam("Real Madrid",27,935)
print(get_all_teams(Che))