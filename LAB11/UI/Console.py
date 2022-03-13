from Controller.ctrl import Controller
from Domain.HospitalDepartment import HospitalDepartments
from Domain.Patients import Patient


class Console:
    def __init__(self, controller: Controller):
        self.__controller = controller

    def print_menu(self):
        print("1. Add a department in repository")
        print("2. Add a patient to department")
        print("3. Update patient")
        print("4. Update Department")
        print("5. Remove patient")
        print("6. Remove department")
        print("7. Sort the patients in a department by personal numerical code")
        print("8. Sort departments by the number of patients")
        print("9. Sort departments by the number of patients having the age above a given limit")
        print("10.Sort departments by the number of patients and the patients in a department alphabetically.")
        print("11.Identify patients from a given department for which the first name or last name contain a given string")
        print("12.Identify department/departments where there are patients with a given first name")
        print("13.Identify departments where there are patients under a given age ")
        print("14.Form groups of k patients from the same department and the same disease ")
        print("15.Form groups of k departments having at most p patients suffering from the same disease")
        print("16.Show all departments ")
        print("17.Show all patients ")

    def run_console(self):
        while True:
            self.print_menu()
            option = input("Introduce the option: ")
            if option == "1":
                self.UI_add_a_department()
            elif option == "2":
                self.UI_add_a_patient()
            elif option == "3":
                self.UI_update_a_patient()
            elif option == "4":
                self.UI_update_a_department()
            elif option == "5":
                self.UI_delete_patient()
            elif option == "6":
                self.UI_delete_department()
            elif option == "7":
                self.UI_SortByNumericalCode()
            elif option == "8":
                self.UI_sortByNumberOfPatients()
            elif option == "9":
                self.UI_sortDepartmentsByPatientsAge()
            elif option == "10":
                self.UI_sort_patients_alphabetically_and_departments_by_number_of_patients()
            elif option == "11":
                self.UI_identify_patients_from_a_given_department_for_which_the_first_name_or_last_name_contain_a_given_string()
            elif option == "12":
                self.UI_identify_departments_where_there_are_patients_with_a_given_first_name()
            elif option == "13":
                self.UI_identify_departments_with_patients_having_an_age_lesser_than_given_age()
            elif option == "14":
                pass
            elif option == "16":
                self.UI_show_all_departments()
            elif option == "17":
                self.UI_show_all_patients()
            elif option == "17":
                break
            else:
                print("Invalid option!")

    def UI_add_a_department(self):
        try:
            id_dep = int(input("Department ID: "))
            name = input("Department name: ")
            bedNumber = int(input("Number of beds in a department: "))
            number_of_patients = int(input("Give the number of patients from the patient list: "))
            patientList = []
            for i in range(number_of_patients):
                print("ADD A PATIENT IN THE LIST: ")
                print('\n')
                patient = self.UI_add_a_patient()
                patientList.append(patient)
            self.__controller.ctrl_add_a_department(id_dep, name, bedNumber, patientList)
        except ValueError as ve:
            print("Error!", ve)
        except Exception as e:
            print("Error!", e)

    def UI_add_a_patient(self):
        try:
            firstName = input("First name: ")
            lastName = input("Last name: ")
            numericalCode = input("Numerical code: ")
            disease = input("Disease: ")
            patient = Patient(firstName, lastName, numericalCode, disease)
            self.__controller.ctrl_add_a_patient(firstName, lastName, numericalCode, disease)
            return patient
        except ValueError as ve:
            print("Error!", ve)
        except Exception as e:
            print("Error!", e)

    def UI_show_all_departments(self):
        list_of_departments = self.__controller.ctrl_show_all_departments()
        for departments in list_of_departments:
            print(departments)

    def UI_show_all_patients(self):
        list_of_patients = self.__controller.ctrl_show_all_patients()
        for patient in list_of_patients:
            print(patient)

    def UI_update_a_patient(self):
        try:
            index = int(input("index= "))
            new_first_name = input("new_first_name= ")
            new_last_name = input("new_last_name= ")
            new_disease = input("new_disease = ")
            self.__controller.ctrl_update_a_patient(index, new_first_name, new_last_name, new_disease)
        except IndexError as ve:
            print("Reintroduce correct values!", ve)
        except Exception as e:
            print("Error!", e)

    def UI_update_a_department(self):
        try:
            index = int(input("index= "))
            new_name = input("new_name= ")
            new_number_of_beds = int(input("new_numbers_of_beds= "))
            self.__controller.ctrl_update_a_department(index, new_name, new_number_of_beds)

        except ValueError as ve:
            print("Reintroduce valid data ! ", ve)
        except Exception as e:
            print("Exception !", e)

    def UI_delete_patient(self):
        try:
            index = int(input("index= "))
            self.__controller.ctrl_delete_patient(index)
        except ValueError as ve:
            print("Reintroduce correct values! ", ve)

    def UI_delete_department(self):
        try:
            index = int(input("index= "))
            self.__controller.ctrl_delete_a_department(index)
        except ValueError as ve:
            print("Reintroduce correct values!", ve)

    def UI_SortByNumericalCode(self):
        sorted_List = self.__controller.ctrl_SortByNumericalCode()
        for patients in sorted_List:
            print(patients)

    def UI_sort_patients_alphabetically_and_departments_by_number_of_patients(self):
        sorted_list = self.__controller.ctrl_sort_patients_alphabetically_and_departments_by_number_of_patients()
        for elements in sorted_list:
            print(elements[0])

    def UI_sortByNumberOfPatients(self):
        sorted_list = self.__controller.ctrl_SortByNumericalCode()
        for elements in sorted_list:
            print(elements[0])

    def UI_sortDepartmentsByPatientsAge(self):
        given_age = int(input("given_age= "))
        sorted_list = self.__controller.ctrl_sort_DepartmentsByPatientsAge(given_age)
        for elem in sorted_list:
            print(f"{elem[0]}, number of patients with their age than given age: {elem[1]}")

    def UI_identify_patients_from_a_given_department_for_which_the_first_name_or_last_name_contain_a_given_string(self):
        try:
            given_string = input("given_string= ")
            id_dep = int(input("Department ID: "))
            name = input("Department name: ")
            bedNumber = int(input("Number of beds in a department: "))
            number_of_patients = int(input("Give the number of patients from the patient list: "))
            patientList = []
            for i in range(number_of_patients):
                print("ADD A PATIENT IN THE LIST: ")
                print('\n')
                patient = self.UI_add_a_patient()
                patientList.append(patient)
            self.__controller.ctrl_add_a_department(id_dep, name, bedNumber, patientList)
            department = HospitalDepartments(id_dep, name, bedNumber, patientList)
            identified_list = self.__controller.ctrl_identify_patients_from_a_given_department_for_which_the_first_name_or_last_name_contain_a_given_string(
                department, given_string)
            for elem in identified_list:
                print(elem)
        except ValueError as ve:
            print("Reintroduce correct data !", ve)
        except Exception as e:
            print("Retry", e)

    def UI_identify_departments_with_patients_having_an_age_lesser_than_given_age(self):
        given_age= int(input("Given_age= "))
        result=self.__controller.ctrl_identify_departments_with_patients_having_an_age_lesser_than_given_age( given_age)
        for res in result:
            print(res)
    def UI_identify_departments_where_there_are_patients_with_a_given_first_name(self):
        given_first_name=input("Given_first_name= ")
        result=self.__controller.ctrl_identify_departments_where_there_are_patients_with_a_given_first_name(given_first_name)
        for res in result:
            print(res)
