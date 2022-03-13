from Domain.HospitalDepartment import HospitalDepartments
from Domain.Patients import Patient
from Utils.SortsAndSearches import bubbleSort, seqSearch


class DepartmentRepository():
    def __init__(self, departments: HospitalDepartments):
        '''
        constructor for repository
        :param departments:
        '''
        self.__departments = departments
        self.__data_storage = []

    def add_a_department(self, Department: HospitalDepartments):
        '''
        add in our repository an instance which is a Hospital Department class
        :param Department:
        :return:
        '''
        for elem in self.__data_storage:
            if Department.get_id() == elem.get_id():
                raise ValueError("The id must be unique!")
        self.__data_storage.append(Department)

    def get_all_departments(self):
        '''
        get all departments
        :return:
        '''
        return self.__data_storage

    def update_a_department(self, index, new_name, new_number_of_beds):
        if index < 0 or index > len(self.__data_storage):
            raise IndexError("Index out of range")
        self.__data_storage[index].set_name(new_name)
        self.__data_storage[index].set_bedNumber(new_number_of_beds)

    def delete_department_by_index(self, index):
        '''
        delete a department from repository
        :param index:
        :return:
        '''
        if index < 0 or index > len(self.__data_storage):
            raise IndexError("Index out of range")
        del self.__data_storage[index]


    def get_department_by_index(self, index):
        '''
        get an department at a given index
        :return:
        '''
        if index < 0 or index > len(self.__data_storage):
            raise IndexError("Index out of range")
        return self.__data_storage[index]

    def len_of_patient_list(self, departament: HospitalDepartments):
        '''
        it used for sorting by the name of patients
        :return:
        '''

        return len(departament.get_all_patients())

    def sort_patients_alphabetically_and_departments_by_number_of_patients(self):
        '''

        :param departments:
        :return:
        '''
        dict_of_departments = {}

        for departments in self.get_all_departments():
            list_of_patients = departments.get_all_patients()
            sorted_list_of_patients = bubbleSort(list_of_patients, lambda x: x.get_firstName()[0])
            dict_of_departments[departments.__str__()] = sorted_list_of_patients

        return bubbleSort(list(dict_of_departments.items()), lambda x: len(x[1]))  # the second element from every tuple

    def sortByNumberOfPatients(self):
        '''
        :return:
        '''

        dict_of_departments = {}
        for departments in self.get_all_departments():
            dict_of_departments[departments.__str__()] = len(departments.get_all_patients())
        return bubbleSort(list(dict_of_departments.items()), lambda x: x[1])

    def sortDepartmentsByPatientsAge(self, given_age):
        dict_of_departments = {}
        for departments in self.get_all_departments():
            number = 0  # It resets at every department
            for patient in departments.get_all_patients():

                if self.obtainAge(patient) > given_age:
                    number = number + 1
            dict_of_departments[departments.__str__()] = number
        return bubbleSort(list(dict_of_departments.items()), condition=lambda x: x[1])

    def obtainAge(self, patient: Patient):
        '''
        obtain age from numerical card
        :return:
        '''
        age = 0
        if patient.get_numericalCode()[0] == '6' or patient.get_numericalCode()[0] == '5':
            digits2 = "20" + str(patient.get_numericalCode()[1]) + str(patient.get_numericalCode()[2])
            age = 2020 - int(digits2)
        elif patient.get_numericalCode()[0] == '1' or patient.get_numericalCode()[0] == '2':
            digits2 = "19" + str(patient.get_numericalCode()[1]) + str(patient.get_numericalCode()[2])
            age = 2020 - int(digits2)
        return age

    def identify_departments_with_patients_having_an_age_lesser_than_given_age(self, given_age):
        departments_list = []
        for departments in self.get_all_departments():
            list_patients = departments.get_all_patients()
            new_list = seqSearch(list_patients, lambda x: self.obtainAge(x) < given_age)
            if len(new_list) > 0:
                departments_list.append(departments)
        return departments_list

    def departmentWithPatientsWithAges(self, department: HospitalDepartments, givenAge):
        nr = 0
        for elem in department.get_all_patients():
            if self.obtainAge(elem) > givenAge:
                nr = nr + 1
        return nr

    def __repr__(self):
        '''
        a string representation
        :return:
        '''
        res = ""
        for elem in self.__data_storage:
            res = res + str(elem)
            res = res + " "
        return res

    def identify_departments_where_there_are_patients_with_a_given_first_name(self, given_first_name):
        '''
        identify departments where there are patients with a given first name
        :param given_first_name:
        :return:
        '''
        list_of_patients_equal_to_given_first_name = []
        for departments in self.get_all_departments():
            list_of_patients = departments.get_all_patients()
            new_list_of_patients = seqSearch(list_of_patients, lambda x: given_first_name == x.get_firstName())
            if len(new_list_of_patients) != 0:
                list_of_patients_equal_to_given_first_name.append(departments)
        return list_of_patients_equal_to_given_first_name

    def identify_patients_from_a_given_department_for_which_the_first_name_or_last_name_contain_a_given_string(self,
                                                                                                               department: HospitalDepartments,
                                                                                                               given_string):
        '''
        identify patients from a given department for which the first name or last name contain a given string
        :param department:
        :param given_string:
        :return:
        '''
        patient_list = department.get_all_patients()
        return seqSearch(patient_list, lambda x: given_string in x.get_firstName() or given_string in x.get_lastName())

'''
j = HospitalDepartments(1, "Andrew", 23)
h = DepartmentRepository(j)
p = Patient("Ceaji", "Lj", "5010321170104", "covid")
q = Patient("Cij", "Lj", "6040321170107", "covid")
r = Patient("Kin", "Lj", "2010321170106", "covid")
s = Patient("Toncea", "Lj", "1910321170105", "covid")
s1 = Patient("Ceaji", "Lj", "2910321170104", "covid")
s2 = Patient("Aeaji", "Lceaj", "2920321170104", "covid")
print(h.obtainAge(p))
k = HospitalDepartments(1, "Andrew", 23)
l = HospitalDepartments(2, "Andrew2", 25)
m = HospitalDepartments(3, "Andrew3", 24)
m.add_a_patient(p)
m.add_a_patient(q)
k.add_a_patient(s)
k.add_a_patient(s1)
k.add_a_patient(s2)
depart_list = DepartmentRepository(j)
depart_list.add_a_department(k)
depart_list.add_a_department(l)
depart_list.add_a_department(m)
print(depart_list.get_all_departments())
result = depart_list.sortDepartmentsByPatientsAge(13)
for depart in result:
    print(f"{depart[0]} number of patients having more than a given age -> {depart[1]}")
result1 = depart_list.sortByNumberOfPatients()
print("****")
print()
for depart in result1:
    print(f" {depart[0]} **** {depart[1]}")
print("***")

print("*********")
result = depart_list.identify_patients_from_a_given_department_for_which_the_first_name_or_last_name_contain_a_given_string(
    k, "qxz")
for i in result:
    print(i)
print("*-*-*-*")
our_result = depart_list.identify_departments_where_there_are_patients_with_a_given_first_name("Ceaji")
for i in our_result:
    print(i)
alpha = depart_list.sort_patients_alphabetically_and_departments_by_number_of_patients()
for item in alpha:
    print(item[0])
    print("***")
    for value in item[1]:
        print(value)
'''