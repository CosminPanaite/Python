class Artist():
    def __init__(self,id,name,style,birth):
        self.__id=id
        self.__name=name
        self.__style=style
        self.__birth=birth
        if type(self.__birth) is not int and self.__birth <0:
            raise ValueError("This must be an int , positive")
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_style(self):
        return self.__style
    def get_birth(self):
        return self.__birth
    def set_id(self,new_id):
        self.__id=new_id
    def set_name(self,new_name):
        self.__name=new_name
    def set_style(self,new_style):
        self.__style=new_style
    def set_birth(self,new_birth):
        self.__birth=new_birth
    def __str__(self):
        return "Artist with id " + str(self.__id) + "Name " + str(self.__name) + " Style " + str(self.__style) + " and birth " + str(self.__birth)
