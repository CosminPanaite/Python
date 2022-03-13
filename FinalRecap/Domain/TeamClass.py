class Team():
    '''
    classdocs
    '''

    def __init__(self, name, score, category):
        self.__name = name
        self.__score = score
        self.__category = category

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, new_name):
        self.__name = new_name

    def set_score(self, new_score):
        self.__score = new_score

    def __str__(self):
        return "The team with the name " + str(self.__name) + "and the score " + str(self.__score)
