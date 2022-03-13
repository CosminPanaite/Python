from Domain.TeamClass import Team
class TeamRepository():
    def __init__(self):
        self.__data_storage=[]
    def add_a_team(self,team:Team):
        if team.get_score()<0:
            raise ValueError("Error!Do not add")
        self.__data_storage.append(team)

    def get_data(self):
        return self.__data_storage
    def delete_team_with_score_under_100(self):
        for i in range(len(self.__data_storage)-1,-1,-1):
            if self.__data_storage[i].get_score()<100:
                del self.__data_storage[i]
    def update_score_of_a_given_team(self,index,new_score):
        self.__data_storage[index].set_score(new_score)
    def filter_score_above_100(self):
        return list(filter(lambda x: x.get_score() >100, self.__data_storage))
    def sort_descending(self):

        return sorted(self.__data_storage,key=lambda x:x.get_score(),reverse=True)
