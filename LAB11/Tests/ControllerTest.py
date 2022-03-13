import unittest

from Controller.ctrl import Controller
from Domain.HospitalDepartment import HospitalDepartments
from Domain.Patients import Patient
from Repository.repo import DepartmentRepository


class ControllerTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__p1 = Patient("Adrian", "Lukas", "5000720140105", "covid")
        self.__p2 = Patient("Adriano", "Luko", "6000574174104", "covid")
        self.__p3 = Patient("Luis", "Fabiano", "2010388888888", "pneumonia")
        self.__p4 = Patient("Adrian", "Lukas", "5000720140105", "covid")
        self.__p5 = Patient("Adriano", "Luko", "6000574174104", "covid")
        self.__p6 = Patient("Luis", "Fabiano", "2010388888888", "pneumonia")
        self.__p7 = Patient("Ruiz", "Jazio", "2010388877888", "pneumonia")
        self.__h1 = HospitalDepartments(1, "Andrew", 23, [self.__p1, self.__p2, self.__p3])
        self.__h2 = HospitalDepartments(2, "Teresa", 35, [self.__p4, self.__p5, self.__p6])
        self.__h3 = HospitalDepartments(3, "Danilo", 30, [])
        self.__dep_repo = DepartmentRepository(self.__h2)
        self.__ctrl_list = Controller(self.__h1, self.__dep_repo)

    def test_ctrl_add_a_department(self):
        self.__p8 = Patient("Gray", "Demaray", "2010388877866", "Flu")
        self.__ctrl_list.ctrl_add_a_department(12, "Shesbury", 22, [self.__p8])
        self.__ctrl_list.ctrl_add_a_department(10, "St Raw", 30, [])
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_departments()), 2)

    def test_ctrl_add_a_patient(self):
        self.__ctrl_list.ctrl_add_a_patient("Julio", "Iglesias", "2010388877865", "Sars")
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_patients()), 4)
        self.__ctrl_list.ctrl_add_a_patient("Julias", "Iglesias", "2010388877864", "Sars")
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_patients()), 5)

    def test_ctrl_show_all_patients(self):
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_patients()), 3)

    def test_ctrl_show_all_departments(self):
        self.__ctrl_list.ctrl_add_a_department(22, "Jia", 300, [])
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_departments()), 1)
        self.__ctrl_list.ctrl_add_a_department(23, "Jia1", 300, [])
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_departments()), 2)
        self.__ctrl_list.ctrl_add_a_department(24, "Jia2", 300, [])
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_departments()), 3)

    def test_ctrl_delete_patient(self):
        self.__ctrl_list.ctrl_delete_patient(0)
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_patients()), 2)
        self.__ctrl_list.ctrl_delete_patient(0)
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_patients()), 1)
        self.__ctrl_list.ctrl_delete_patient(0)
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_patients()), 0)

    def test_ctrl_delete_department(self):
        self.__ctrl_list.ctrl_add_a_department(22, "Jia", 300, [])
        self.__ctrl_list.ctrl_add_a_department(23, "Jia", 300, [])
        self.__ctrl_list.ctrl_delete_a_department(0)
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_departments()), 1)
        self.__ctrl_list.ctrl_add_a_department(24, "Jia", 300, [])
        self.__ctrl_list.ctrl_delete_a_department(0)
        self.assertEqual(len(self.__ctrl_list.ctrl_show_all_departments()), 1)

    def test_ctrl_SortByNumericalCode(self):
        lst = self.__ctrl_list.ctrl_SortByNumericalCode()
        self.assertEqual(lst[0][0],
                         'Patient with name Luis Fabiano with numerical code 2010388888888 and with the disease pneumonia')
        self.assertEqual(lst[1][0],
                         'Patient with name Adrian Lukas with numerical code 5000720140105 and with the disease covid')
        self.assertEqual(lst[2][0],
                         'Patient with name Adriano Luko with numerical code 6000574174104 and with the disease covid')

    def test_ctrl_sort_patients_alphabetically_and_departments_by_number_of_patients(self):
        self.__ctrl_list.ctrl_add_a_department(11, "Jake", 200, [self.__p1, self.__p2])
        self.__ctrl_list.ctrl_add_a_department(22, "Take", 30, [self.__p3, self.__p4, self.__p5])
        lst = self.__ctrl_list.ctrl_sort_patients_alphabetically_and_departments_by_number_of_patients()
        self.assertEqual(lst[0][0],
                         "The departaments identified by id 11 the name  Jake the number of beds 200 the list of patients"
                         " ['Patient with name Adrian Lukas with numerical code 5000720140105 and with the disease covid',"
                         " 'Patient with name Adriano Luko with numerical code 6000574174104 and with the disease covid']")
    def test_ctrl_sort_DepartmentsByPatientsAge(self):
        self.__ctrl_list.ctrl_add_a_department(11, "Jake", 200, [self.__p1, self.__p2])
        self.__ctrl_list.ctrl_add_a_department(22, "Take", 30, [self.__p3, self.__p4, self.__p5])

        lst=self.__ctrl_list.ctrl_sort_DepartmentsByPatientsAge(0)
        self.assertEqual(len(lst),2)
        self.assertEqual(lst[0][0],"The departaments identified by id 11 the name  Jake the number of beds 200 the list of patients ['Patient with name Adrian Lukas with numerical code 5000720140105 and with the disease covid', 'Patient with name Adriano Luko with numerical code 6000574174104 and with the disease covid']")
        self.assertEqual(lst[0][1],2)
    def test_ctrl_sortByNumberOfPatients(self):
        self.__ctrl_list.ctrl_add_a_department(11, "Jake", 200, [self.__p1, self.__p2])
        self.__ctrl_list.ctrl_add_a_department(22, "Take", 30, [self.__p3, self.__p4, self.__p5])
        lst=self.__ctrl_list.ctrl_sortByNumberOfPatients()
        self.assertEqual(lst[0][0],("The departaments identified by id 11 the name  Jake the number of beds 200 the list of patients ['Patient with name Adrian Lukas with numerical code 5000720140105 and with the disease covid', 'Patient with name Adriano Luko with numerical code 6000574174104 and with the disease covid']"))
    def test_ctrl_identify_patients_from_a_given_department_for_which_the_first_name_or_last_name_contain_a_given_string(self):
        patient1 = Patient("Jake","Fin","6010322270103","covid")
        patient2 = Patient("Jake", "Fin", "6010322270104", "covid")
        depart=HospitalDepartments(11,"Kalius",30,[patient1,patient2])

        lst=self.__ctrl_list.ctrl_identify_patients_from_a_given_department_for_which_the_first_name_or_last_name_contain_a_given_string(depart,"Jake")
        self.assertEqual(len(lst),2)

    def test_ctrl_identify_departments_with_patients_having_an_age_lesser_than_given_age(self):
        p=Patient("Jay","Kay","1010321150104","None")
        self.__ctrl_list.ctrl_add_a_department(11, "Jake", 200, [self.__p1, self.__p2])
        self.__ctrl_list.ctrl_add_a_department(12,"Rake",300,[p])
        lst=self.__ctrl_list.ctrl_identify_departments_with_patients_having_an_age_lesser_than_given_age(71)
        self.assertEqual(len(lst),1)
    
if __name__ == "__main__":
    unittest.main()
