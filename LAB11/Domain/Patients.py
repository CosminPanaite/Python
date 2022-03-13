from numpy.core.defchararray import isdigit


class Patient:
    def __init__(self, firstName, lastName, numericalCode, disease):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__numericalCode = numericalCode
        self.__disease = disease
        if type(firstName) is not str:
            raise ValueError("First name must be a string")
        if type(lastName) is not str:
            raise ValueError("Last name must be a string")
        if type(numericalCode) is not str or len(numericalCode) != 13 or isdigit(numericalCode) == False:
            raise ValueError("Numerical code must be a int and contain 13 digits")

        if type(disease) is not str:
            raise ValueError("Disease must be a string")

    def get_firstName(self):
        return self.__firstName

    def set_firstName(self, newFirstName):
        if type(newFirstName) is not str:
            raise ValueError("First name must be a string")
        self.__firstName = newFirstName

    def get_lastName(self):
        return self.__lastName

    def set_lastName(self, newLastName):
        '''
        setter method for new last name
        :param newLastName:
        :return:
        '''
        if type(newLastName) is not str:
            raise ValueError("First name must be a string")
        self.__lastName = newLastName

    def get_numericalCode(self):
        '''
        getter method for numerical Code
        '''
        return self.__numericalCode

    def set_numericalCode(self):
        '''
        setter method for numerical
        :return:
        '''
        if type(numericalCode) is not str:
            raise ValueError("Numerical code must be a int")

    def get_disease(self):
        '''
        getter method for disease
        :return:
        '''
        return self.__disease

    def set_disease(self, newDisease):
        if type(newDisease) is not str:
            raise ValueError("Disease must be a string")
        self.__disease = newDisease

    def __str__(self):

        return "Patient with name " + str(self.__firstName) + " " + str(
            self.__lastName) + " with numerical code " + str(
            self.__numericalCode) + " and with the disease " + str(self.__disease)


