class Shop():
    def __init__(self,id,name,location,list_of_products):
        self.__id=id
        self.__name=name
        self.__location=location
        self.__list_of_products=list_of_products
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_location(self):
        return self.__location
    def get_list_of_products(self):
        return self.__list_of_products
    def set_id(self,new_id):
        self.__id=new_id
    def set_name(self,new_name):
        self.__name=new_name
    def set_location(self,new_loc):
        self.__location=new_loc
    def set_list_of_products(self,new_list):
        self.__list_of_products=new_list
    def __str__(self):

        return "The shop with id " + str(self.__id) + " name " + str(self.__name) + " location  " + str(self.__location) + " list of products  " + str(self.__list_of_products)
