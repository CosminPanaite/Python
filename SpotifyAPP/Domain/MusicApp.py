class MusicApp():
    def __init__(self,name:(str),views,category):
        self.__name=name
        self.__views=views
        self.__category=category
    def get_name(self):
        return self.__name
    def get_views(self):
        return self.__views
    def get_category(self):
        return self.__category
    def set_name(self,new_n):
        self.__name=new_n
    def set_views(self,new_views):
        self.__views=new_views
    def set_category(self,new_c):
        self.__category=new_c
    def __str__(self):
        return "Song with name " + str(self.__name) + " nr views " + str(self.__views) + " // "