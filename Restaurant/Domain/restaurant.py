class Restaurant():
    def __init__(self,name,calories,category):
        self.__name=name
        self.__calories=calories
        self.__category=category
    def get_name(self):
        return self.__name
    def get_calories(self):
        return self.__calories
    def get_category(self):
        return self.__category
    def set_name(self,new_name):
        self.__name=new_name
    def set_calories(self,new_calories):
        self.__calories=new_calories
    def set_category(self,new_category):
        self.__category=new_category
    def __str__(self):
        return "Dish with name " + str(self.__name) + " and " + str(self.__calories) +" calories "
