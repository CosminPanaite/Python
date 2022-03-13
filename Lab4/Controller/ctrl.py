from Domain.MyVector import MyVector
from Domain.Validator import VectorValidator
from Repository.repo import VectorRepository


class VectorController:
    def __init__(self, data_storage: VectorRepository, vector_validator: VectorValidator):
        '''
        constructor
        :param data_storage:
        :param vector_validator:
        '''
        self.__data_storage = data_storage
        self.__vector_validator = vector_validator

    def ctrl_add_a_vector(self, name_id, colour, vector_type, values):
        '''
        add a vector in the repository
        :param name_id:
        :param colour:
        :param vector_type:
        :param values:
        :return:
        '''
        vector = MyVector(name_id, colour, vector_type, values)
        self.__vector_validator.validate_vector(vector)
        self.__data_storage.add_a_vector(vector)

    def ctrl_get_all_vectors(self):
        '''
        get all vectors from list
        :return:
        '''
        return self.__data_storage.get_all_vectors()
    def ctrl_get_a_vector_at_an_index(self,index):
        '''
        get a vector at a given index
        :param index:
        :return:
        '''
        return self.__data_storage.get_a_vector_at_an_index(index)
    def ctrl_update_a_vector(self,index, new_colour, new_vector_type, new_values):
        '''
        update a vector
        :param index:
        :param new_colour:
        :param new_vector_type:
        :param new_values:
        :return:
        '''
        self.__data_storage.update_a_vector(index, new_colour, new_vector_type, new_values)
    def ctrl_update_a_vector_by_name(self,name_id, new_colour, new_vector_type, new_values):
        '''
        update a vector by name_id
        :param name_id:
        :param new_colour:
        :param new_vector_type:
        :param new_values:
        :return:
        '''
        self.__data_storage.update_a_vector_by_name(name_id,new_colour,new_vector_type,new_values)
    def ctrl_delete_a_vector_by_index(self,index):
        '''
        delete a vector by index
        :param index:
        :return:
        '''
        self.__data_storage.delete_a_vector_by_index(index)
    def ctrl_delete_a_vector_by_name(self,name_id):
        '''
        delete a vector by name_id
        :param name_id:
        :return:
        '''
        self.__data_storage.delete_a_vector_by_name(name_id)
    def ctrl_get_the_sum_of_all_vectors(self):
        '''
        Get the vector which represents the sum of all vectors

        :return:
        '''
        return self.__data_storage.get_the_sum_of_all_vectors()
    def ctrl_get_the_list_of_vector_with_minimum_elements(self,given_min):
        '''
        get the list of vectors having the minimum less than a given value
        :param given_min:
        :return:
        '''
        return self.__data_storage.get_the_list_of_vector_with_minimum_elements(given_min)
    def ctrl_plot_vectors(self):
        '''
        plot all vectors
        :return:
        '''
        self.__data_storage.plot_vectors()