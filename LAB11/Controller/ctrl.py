from Domain.HospitalDepartment import HospitalDepartments
from Domain.Patients import Patient
from Repository.repo import DepartmentRepository


class Controller():
    def __init__(self, hospital_departments: HospitalDepartments, department_repository: DepartmentRepository):
        '''

        :param hospital_departments:
        :param department_repository:
        '''
        self.__hospital_departments = hospital_departments
        self.__department_repository = department_repository

    def ctrl_add_a_department(self, id_dep, name, bedNumber, patientList):
        '''
        
        :param id_dep: 
        :param name: 
        :param bedNumber: 
        :return: 
        '''
        department = HospitalDepartments(id_dep, name, bedNumber, patientList)
        self.__department_repository.add_a_department(department)

    def ctrl_add_a_patient(self, firstName, lastName, numericalCode, disease):
        '''
        add a new patient
        :param firstName: 
        :param lastName: 
        :param numericalCode:
        :param disease: 
        :return: 
        '''
        patient = Patient(firstName, lastName, numericalCode, disease)
        self.__hospital_departments.add_a_patient(patient)

    def ctrl_show_all_patients(self):
        '''
        obtain all patients
        :return:
        '''
        return self.__hospital_departments.get_all_patients()

    def ctrl_show_all_departments(self):
        '''
        obtain all departments
        :return:
        '''
        return self.__department_repository.get_all_departments()
    def ctrl_update_a_patient(self, index, new_first_name, new_last_name, new_disease):
        '''
        update a patient
        :param index:
        :param new_first_name:
        :param new_last_name:
        :param new_disease:
        :return:
        '''
        self.__hospital_departments.update_a_patient(index,new_first_name,new_last_name,new_disease)
    def ctrl_update_a_department(self, index, new_name, new_number_of_beds):
        '''
        update a department
        :param index:
        :param new_name:
        :param new_number_of_beds:
        :return:
        '''
        self.__department_repository.update_a_department(index,new_name,new_number_of_beds)
    def ctrl_delete_patient(self, index):
        '''
        delete a patient
        :param index:
        :return:
        '''
        self.__hospital_departments.delete_patient(index)
    def ctrl_delete_a_department(self,index):
        '''
        delete a department
        :param index:
        :return:
        '''
        self.__department_repository.delete_department_by_index(index)
    def ctrl_SortByNumericalCode(self):
        '''
        Sort patients by numerical code
        :return:
        '''
        return self.__hospital_departments.SortByNumericalCode()
    def ctrl_sort_patients_alphabetically_and_departments_by_number_of_patients(self):
        '''
        sort alphabetically
        :return:
        '''
        return self.__department_repository.sort_patients_alphabetically_and_departments_by_number_of_patients()
    def ctrl_sortByNumberOfPatients(self):
        return self.__department_repository.sortByNumberOfPatients()

    def ctrl_sort_DepartmentsByPatientsAge(self,given_age):
        return self.__department_repository.sortDepartmentsByPatientsAge(given_age)
    def ctrl_identify_patients_from_a_given_department_for_which_the_first_name_or_last_name_contain_a_given_string(self,department: HospitalDepartments,
                                                                                                               given_string):
        return self.__department_repository.identify_patients_from_a_given_department_for_which_the_first_name_or_last_name_contain_a_given_string(department,given_string)
    def ctrl_identify_departments_with_patients_having_an_age_lesser_than_given_age(self,given_age):
        return self.__department_repository.identify_departments_with_patients_having_an_age_lesser_than_given_age(given_age)
    def ctrl_identify_departments_where_there_are_patients_with_a_given_first_name(self, given_first_name):
        return self.__department_repository.identify_departments_where_there_are_patients_with_a_given_first_name(given_first_name)
