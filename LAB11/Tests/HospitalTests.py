import unittest
from Domain.HospitalDepartment import HospitalDepartments
from Domain.Patients import Patient


class HospitalTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__p1 = Patient("Adrian", "Lukas", "5000720140105", "covid")
        self.__p2 = Patient("Adriano", "Luko", "6000574174104", "covid")
        self.__p3 = Patient("Luis", "Fabiano", "2010388888888", "pneumonia")
        self.__p4 = Patient("Adrian", "Lukas", "5000720140105", "covid")
        self.__p5 = Patient("Adriano", "Luko", "6000574174104", "covid")
        self.__p6 = Patient("Luis", "Fabiano", "2010388888888", "pneumonia")
        self.__p7 = Patient("Ruiz", "Jazio", "2010388877888", "pneumonia")
        self.__h1 = HospitalDepartments(1, "Andrew", 23 ,[self.__p1,self.__p2,self.__p3])
        self.__h2 = HospitalDepartments(2, "Teresa", 35, [self.__p4,self.__p5,self.__p6])
        self.__h3 = HospitalDepartments(3, "Danilo" ,30, [])
    def test_add_a_patient(self):
        pat=Patient("Gustavo","Luiz","1010321140102","Flu")
        self.__h1.add_a_patient(self.__p7)
        self.assertEqual(len(self.__h1.get_all_patients()),4)
        self.__h2.add_a_patient(pat)
        self.assertEqual(len(self.__h2.get_all_patients()),4)
    def test_get_all_patients(self):
        self.assertEqual(len(self.__h1.get_all_patients()),3)
        self.assertEqual(len(self.__h3.get_all_patients()),0)
    def testupdate_a_patient(self):
        self.__h1.update_a_patient(0,"Darke","Diop","Pneumonia")
        self.assertEqual(self.__p1.get_firstName(),"Darke")
        self.assertEqual(self.__p1.get_lastName(), "Diop")
    def test_delete_a_patient(self):
        self.__h2.delete_patient(0)
        self.assertEqual(len(self.__h2.get_all_patients()),2)
        self.__h2.delete_patient(1)
        self.assertEqual(len(self.__h2.get_all_patients()), 1)
    def test_SortByNumericalCode(self):
        lst1=self.__h2.SortByNumericalCode()
        self.assertEqual(lst1[0][0],'Patient with name Luis Fabiano with numerical code 2010388888888 and with the disease pneumonia')
        self.assertEqual(lst1[0][1],'2')
        self.assertEqual(lst1[1][0],"Patient with name Adrian Lukas with numerical code 5000720140105 and with the disease covid")


if __name__ == "__main__":
    unittest.main()
