from Domain.Boat import Boat


class Repo():
    def __init__(self):
        self.__data_storage = []

    def add_a_boat(self, boat: Boat):
        self.__data_storage.append(boat)

    def get_all_boats(self):
        return self.__data_storage

    def update(self, tip, new_id, new_speed):
        for elem in self.__data_storage:
            if elem.get_tipe() == tip:
                elem.set_id(new_id)
                elem.set_speed(new_speed)

    def delete(self):
        nr = 0
        for elem in range(len(self.__data_storage) - 1, -1, -1):
            if self.__data_storage[elem].get_rented() != False:
                del self.__data_storage[elem]
                nr = nr + 1
        if nr == len(self.__data_storage):
            raise ValueError("This is unmodified")

    def sort_unrented(self):
        lst = []
        for elem in self.__data_storage:
            if elem.get_rented == False:
                lst.append(elem)
        return sorted(lst, key=lambda x: x.get_speed())

    def identify_givven(self, given_speed):
        return list(filter(lambda x: x.get_speed() > given_speed, self.__data_storage))
