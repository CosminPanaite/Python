import numpy as np


class MyVector:
    def __init__(self, name_id, colour, vector_type, values):
        '''
        a constructor for class MyVector
        :param name_id:
        :param colour:
        :param vector_type:
        :param values:
        '''
        self.__name_id = name_id
        self.__colour = colour
        self.__vector_type = vector_type
        self.__values = np.array(values)

    def get_name_id(self):
        '''
        getter method
        :return:
        '''
        return self.__name_id

    def get_colour(self):
        '''

        :return:
        '''
        return self.__colour

    def get_vector_type(self):
        '''

        :return:
        '''
        return self.__vector_type

    def get_values(self):
        '''
        setter method for values

        :return:
        '''
        return self.__values

    def set_name_id(self, new_name_id):
        '''
        setter method for name_id
        :param new_name_id:
        :return:
        '''
        if type(new_name_id) not in [str, int]:
            raise ValueError("Reintroduce a valid value!")
        self.__name_id = new_name_id

    def set_colour(self, new_colour):
        '''
        setter method for colour
        :param new_colour: a new given colour
        :return:
        '''
        self.__colour = new_colour

    def set_vector_type(self, new_vector_type):
        '''
        setter method for vector type
        :param new_vector_type: a new type of vector
        :return:
        '''
        self.__vector_type = new_vector_type

    def set_values(self, new_values):
        '''
        setter method for values
        :param new_values: a new list of values
        :return:
        '''

        self.__values = np.array(new_values)

    def add_a_scalar(self, scalar):
        '''
        add a scalar in a vector
        :return:the result of the operation

        '''

        self.__values = self.__values + scalar
        return self.__values

    def add_two_vectors(self, vector):
        '''
        add 2 vectors
        :param vector: an object of class
        :return: the result of the operation
        '''

        if len(self.__values) != len(vector.get_values()):
            raise ValueError("They should have the same lenght")
        else:
            self.__values = self.__values + vector.get_values()
            return self.__values

    def subtract_two_vectors(self, vector):
        '''
        subtract 2 vectors
        :param vector:
        :return: the result of the operation
        '''
        if len(self.__values) != len(vector.get_values()):
            raise ValueError("They should have the same lenght")

        else:
            self.__values = self.__values - vector.get_values()
            return self.__values

    def multiplication_of_vectors(self, vector):
        '''
        multiply 2 vectors
        :param vector: an object of class
        :return: the result of the operation
        '''
        if len(self.__values) != len(vector.get_values()):
            raise ValueError("They should have the same lenght")

        else:
            prod = self.__values.dot(vector.get_values())
            return prod

    def sum_of_array(self):
        '''
        return the sum of all elements of all vectors
        :return:    the sum of all elements of all vectors
        '''
        if len(self.__values) == 0:
            raise IndexError(" The values list of the vector is empty.")

        return self.__values.sum()

    def minim_of_array(self):
        '''
        computes the minimum of arrays
        :return: the minimum
        '''
        if len(self.__values) == 0:
            raise IndexError(" The values list of the vector is empty.")

        return self.__values.min()

    def maxim_of_array(self):
        '''
        it computes the maximum of elements from a numpy array
        :return: the maximum
        '''
        if len(self.__values) == 0:
            raise IndexError(" The values list of the vector is empty.")

        return self.__values.max()

    def average_of_array(self):
        '''
        it computes the average of elements from a numpy array
        :return: the average of elements from lists
        '''
        if len(self.__values) == 0:
            raise IndexError(" The values list of the vector is empty.")
        return np.average(self.__values)

    def product_of_array(self):
        '''
        product of elements from an numpy array
        :return: the product
        '''
        if len(self.__values) == 0:
            return 0
        return self.__values.prod()


    def __str__(self):
        '''
        a string representation of class MyVector
        :return:
        '''
        return "The vector of ID: " + str(self.__name_id) + " of COLOUR: " + str(self.__colour) + " of TYPE: " + str(
            self.__vector_type) + " with the VALUES: " + str(self.__values)
