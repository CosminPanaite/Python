class Boat():
    def __init__(self,id,tipe,speed,rented):
        self.__id=id
        self.__tipe=tipe
        self.__speed=speed
        self.__rented=rented
        if type(speed) is not float:
            raise ValueError("This must be a float!")
        if type(self.__rented) is not bool:
            raise ValueError("This must be a bool!")
    def get_id(self):
        return self.__id
    def get_tipe(self):
        return self.__tipe
    def get_speed(self):
        return self.__speed
    def get_rented(self):
        return self.__rented

    def set_id(self,new_id):
        self.__id=new_id

    def set_tipe(self,new_tipe):
        self.__tipe=new_tipe

    def set_speed(self,new_speed):
        if type(new_speed) is not float:
            raise ValueError("This must be a float!")
        self.__speed=new_speed

    def set_rented(self,new_rented):
        if type(new_rented) is not bool:
            raise ValueError("This must be a bool!")
        self.__rented=new_rented
    def __str__(self):
        return "The boat with " + str(self.__id) + " with speed  " + str(self.__speed) + " with tipe  " + str(self.__tipe) + " and is rented " + str(self.__rented)
