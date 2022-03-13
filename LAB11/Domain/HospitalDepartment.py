from Domain.Patients import Patient
from Utils.SortsAndSearches import bubbleSort


class HospitalDepartments:
    def __init__(self, id_dep, name, bedNumber, patientList):
        self.__id_dep = id_dep
        self.__name = name
        self.__bedNumber = bedNumber
        self.__patientList = patientList
        if type(id_dep) is not int:
            raise ValueError("It should be an integer")
        if type(name) is not str:
            raise ValueError("It should be an str instance")
        if type(bedNumber) is not int:
            raise ValueError("It should be an integer")

    def get_id(self):
        '''
        getter method for id
        :return:
        '''
        return self.__id_dep

    def set_id(self, new_id):
        '''
        set method for a new id
        :param new_id:
        :return:
        '''
        if type(new_id) is not int:
            raise ValueError("It should be an integer")
        self.__id_dep = new_id

    def get_name(self):
        '''
        getter method for name
        :return:
        '''
        return self.__name

    def set_name(self, new_name):
        '''
        set method for a new id
        :param new_id:
        :return:
        '''
        if type(new_name) is not str:
            raise ValueError("It should be a str type")
        self.__name = new_name

    def get_bedNumber(self):
        '''
        getter method for number of beds
        :return:
        '''
        return self.__bedNumber

    def set_bedNumber(self, new_bedNumber):
        '''
        setter method for number of beds
        :param new_bedNumber:
        :return:
        '''
        if type(new_bedNumber) is not int:
            raise ValueError("It should be an integer")
        self.__bedNumber = new_bedNumber

    def add_a_patient(self, patient: Patient):
        '''
        add a patient in list of patients
        :param patient:
        :return:
        '''
        for p in self.__patientList:
            if patient.get_numericalCode() == p.get_numericalCode():
                raise ValueError("The numerical code should be unique")
        self.__patientList.append(patient)

    def get_all_patients(self):
        '''
        it returns all the patients
        :return:
        '''
        return self.__patientList

    def update_a_patient(self, index, new_first_name, new_last_name, new_disease):
        '''
        this function updates a patient
        :param index:
        :param new_first_name:
        :param new_last_name:
        :param new_disease:
        :return:
        '''
        if index < 0 or index > len(self.__patientList):
            raise IndexError("Index out of range")
        if type(new_first_name) is not str:
            raise ValueError("This must be a string")
        if type(new_last_name) is not str:
            raise ValueError("This must be a string")
        if type(new_disease) is not str:
            raise ValueError("This must be a string")
        self.__patientList[index].set_firstName(new_first_name)
        self.__patientList[index].set_lastName(new_last_name)
        self.__patientList[index].set_disease(new_disease)

    def delete_patient(self, index):
        '''
        this function removes a patient at a given index
        :param index:
        :return:
        '''
        if index < 0 or index > len(self.__patientList) - 1:
            raise ValueError("We can't remove patients out of range")
        del self.__patientList[index]

    def SortByNumericalCode(self):
        '''

        :return:
        '''
        dict_of_patient = {}
        for patient in self.get_all_patients():
            dict_of_patient[patient.__str__()] = patient.get_numericalCode()[0]
        return bubbleSort(list(dict_of_patient.items()), lambda x: x[1])

    def __repr__(self):
        result = []
        for elem in self.get_all_patients():
            result.append(str(elem))
        return "The departaments identified by id " + str(self.__id_dep) + " the name " + " " + str(
            self.__name) + " the number of beds " + str(self.__bedNumber) + " the list of patients " + str(result)
