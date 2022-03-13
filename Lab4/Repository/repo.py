import matplotlib.pyplot as plt
from Domain.MyVector import MyVector
from Domain.Validator import VectorValidator


class VectorRepository:
    '''
    A vector repository is a structure that manages multiple vectors of class MyVector
    '''

    def __init__(self, validator: VectorValidator):
        '''
        Create a new instance of VectorRepository
        '''
        self.__data_storage = []
        self.__validator = validator

    def __str__(self):
        '''
        a string method for list of vectors
        :return:
        '''
        result = " "

        for vector in self.__data_storage:
            result = result + str(vector)
            result = result + " ; "
        return result

    def add_a_vector(self, vector: MyVector):
        '''
        add a new vector in the list
        :param vector: an object of class
        :return: it adds a vectors
        '''

        ok = 1
        for vec in self.__data_storage:
            if vec.get_name_id() == vector.get_name_id():
                ok = 0
        if ok == 0:
            raise ValueError("The introduced ID already exists! Retry")
        self.__validator.validate_vector(vector)
        self.__data_storage.append(vector)

    def get_all_vectors(self):
        '''
        it returns all vectors from list
        :return: return the list of all vectors
        '''
        return self.__data_storage

    def get_a_vector_at_an_index(self, index):
        '''
        it returns an element from an given index from list
        :param index: a given index
        :return: returns the element of index (index)
        '''
        if index < 0 or index > len(self.__data_storage) - 1:
            raise IndexError("There is no vector corresponding to the given index.")

        return self.__data_storage[index]

    def update_a_vector(self, index, new_colour, new_vector_type, new_values):
        '''
        Update a vector
        :param index: a given index
        :param new_colour: a new colour given
        :param new_vector_type: a new vector type given
        :param new_values: a list of new values given
        :return:
        '''
        if index < 0 or index > len(self.__data_storage) - 1:
            raise IndexError("There is no vector corresponding to the given index.")
        self.__validator.validate_vector(self.__data_storage[index])
        self.__data_storage[index].set_colour(new_colour)
        self.__data_storage[index].set_vector_type(new_vector_type)
        self.__data_storage[index].set_values(new_values)

    def update_a_vector_by_name(self, name_id, new_colour, new_vector_type, new_values):
        '''
        it updates vector by unique attribute name_id
        :param name_id: a given name_id
        :param new_colour: a new colour given
        :param new_vector_type: a new type given
        :param new_values: a new list of values given
        :return:
        '''
        for elem in self.__data_storage:
            if elem.get_name_id() == name_id:
                elem.set_colour(new_colour)
                elem.set_vector_type(new_vector_type)
                elem.set_values(new_values)
                self.__validator.validate_vector(elem)

    def delete_a_vector_by_index(self, index):
        '''
        delete a vector by a given index
        :param index: a given index
        '''
        if index < 0 or index > len(self.__data_storage) - 1:
            raise IndexError("There is no vector corresponding to the given index.")
        del self.__data_storage[index]

    def delete_a_vector_by_name(self, name_id):
        '''
        delete vector by name
        :param name_id: a given name id
        :param vector: an object of class
        '''
        list_of_name_id = [vector.get_name_id() for vector in self.get_all_vectors()]
        if name_id not in list_of_name_id:
            raise ValueError("The name_id doesn't exist in the storage!")
        for elem in range(len(self.__data_storage) - 1, -1, -1):
            if self.__data_storage[elem].get_name_id() == name_id:
                del self.__data_storage[elem]

    def plot_vectors(self):
        '''
        plot all vectors in chart and give them a form with the aid of their type
        :return:
        '''
        list_of_vectors = self.get_all_vectors()
        if len(list_of_vectors) == 0:
            raise ValueError("The list doesn't have any vector!")
        for vec in list_of_vectors:
            if vec.get_vector_type() == 1:
                type_model = 'o'
            elif vec.get_vector_type() == 2:
                type_model = 's'
            elif vec.get_vector_type() == 3:
                type_model = '^'
            elif vec.get_vector_type() > 3:
                type_model = 'D'
            plt.plot(vec.get_values(), vec.get_colour(), marker=type_model, linestyle='')
        plt.show()

    def get_the_sum_of_all_vectors(self):
        '''
        obtain the sum of lists and set the attributes of the vector as the first one
        :return: updated vector where we compute the sum of lists
        '''
        list_of_values = [vector.get_values() for vector in self.get_all_vectors()]
        if len(list_of_values) == 0:
            raise ValueError("The list should contain elements")
        else:
            first = len(list_of_values[0])
            ok = True
            for arr in list_of_values:
                if len(arr) != first:
                    ok = False
            if ok == False:
                raise ValueError("Lists shoud have the same length")
        s = 0
        s2 = 0
        if len(self.__data_storage) == 0:
            raise ValueError("The list should contain elements")
        if len(self.__data_storage) == 1:
            return self.__data_storage[0]
        elif len(self.__data_storage) == 2:
            s = self.__data_storage[0].get_values() + self.__data_storage[1].get_values()
            n_id = self.__data_storage[0].get_name_id()
            clr = self.__data_storage[0].get_colour()
            typ = self.__data_storage[0].get_vector_type()
            vv = MyVector(n_id, clr, typ, s)
            return vv
        else:
            s = s + self.__data_storage[0].get_values() + self.__data_storage[1].get_values()
            for elem in range(2, len(self.__data_storage)):
                s2 += self.__data_storage[elem].get_values() + s
                n_id = self.__data_storage[0].get_name_id()
                clr = self.__data_storage[0].get_colour()
                typ = self.__data_storage[0].get_vector_type()
                vv2 = MyVector(n_id, clr, typ, s2)
            return vv2

    def get_the_list_of_vector_with_minimum_elements(self, given_min):
        '''
        Return the list of vectors having the minimum less than a given value.
        :param given_min: a given value for minimum
        :return: the updated list of vectors
        '''
        if len(self.__data_storage) == 0:
            raise ValueError("The list shoud not be empty")
        for elem in range(len(self.__data_storage) - 1, -1, -1):
            if self.__data_storage[elem].minim_of_array() >= given_min:
                del (self.__data_storage[elem])
        return self.__data_storage
