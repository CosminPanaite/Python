import unittest
from Domain.MyVector import MyVector
from Domain.Validator import VectorValidator
from Repository.repo import VectorRepository


class TestRepo(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__v = MyVector(2, "m", 22, [40, 53, 41])
        self.__v2 = MyVector(1, "m", 4, [22, 33, 2])
        self.__v3 = MyVector(55, "r", 10, [30, 40, 20, 50])
        self.__v4 = MyVector(3, "m", 10, [30, 40, 20, 50])
        self.__v5 = MyVector(7, "g", 15, [2])
        self.__v6 = MyVector(9, "y", 4, [5])
        self.__v7 = MyVector(11, "y", 4, [])
        self.__v8 = MyVector(22, "y", 4, [10, 20, 30])
        self.__v9 = MyVector(13, "m", 445, [])
        self.__v10 = MyVector(100, "y", 3, [])
        self.__v11 = MyVector(101, "y", 4, [25, 26])
        self.__vs1 = MyVector(102, "r", 5, [2])
        self.__vs2 = MyVector(103, "r", 8, [4])
        self.__vs3 = MyVector(104, "r", 9, [2])
        self.__vs4 = MyVector(105, "y", 10, [4, 2])
        self.__vs5 = MyVector(106, "g", 11, [2, 2])
        self.__vs6 = MyVector(108, "y", 12, [4, 33])
        self.__vs7 = MyVector(109, "y", 12, [4, 33])
        self.__list_validator = VectorValidator()
        self.__list_of_vectors = VectorRepository(self.__list_validator)
        self.__list_of_vectors2 = VectorRepository(self.__list_validator)
        self.__list_of_vectors3 = VectorRepository(self.__list_validator)
        self.__list_of_vectors4 = VectorRepository(self.__list_validator)
        self.__list_of_vectors5 = VectorRepository(self.__list_validator)
        self.__list_of_vectors6 = VectorRepository(self.__list_validator)
        self.__list_of_vs1= VectorRepository(self.__list_validator)
        self.__list_of_vs2 = VectorRepository(self.__list_validator)
        self.__list_of_vs3 = VectorRepository(self.__list_validator)
        self.__list_of_vs4 = VectorRepository(self.__list_validator)
        self.__list_of_vs5 = VectorRepository(self.__list_validator)
        self.__list_of_vectors.add_a_vector(self.__v)
        self.__list_of_vectors.add_a_vector(self.__v2)
        self.__list_of_vectors.add_a_vector(self.__v3)
        self.__list_of_vectors2.add_a_vector(self.__v4)
        self.__list_of_vectors3.add_a_vector(self.__v6)
        self.__list_of_vectors4.add_a_vector(self.__v8)
        self.__list_of_vectors4.add_a_vector(self.__v9)
        self.__list_of_vectors4.add_a_vector(self.__v10)
        self.__list_of_vectors5.add_a_vector(self.__v)
        self.__list_of_vectors5.add_a_vector(self.__v2)
        self.__list_of_vectors6.add_a_vector(self.__v3)
        self.__list_of_vectors6.add_a_vector(self.__v4)
        self.__list_of_vs1.add_a_vector(self.__vs1)
        self.__list_of_vs2.add_a_vector(self.__vs1)
        self.__list_of_vs2.add_a_vector(self.__vs2)
        self.__list_of_vs3.add_a_vector(self.__vs3)
        self.__list_of_vs4.add_a_vector(self.__vs7)
        self.__list_of_vs4.add_a_vector(self.__v8)
        self.__list_of_vs5.add_a_vector(self.__vs5)

        self.__mylist = []
        self.__mylist1 = []
        self.__result = self.__list_of_vectors.get_all_vectors()
        self.__result2 = self.__list_of_vectors2.get_all_vectors()

    def tearDown(self):
        unittest.TestCase.tearDown(self)
    def test_add_a_vector(self):
        self.__va1 = MyVector(1105, "y", 10, [4, 2])
        self.__va2 = MyVector(1106, "g", 11, [2, 2])
        self.__va3 = MyVector(1108, "y", 12, [4, 33])
        self.__va4 = MyVector(1109, "y", 12, [4, 33])
        self.__va5  = MyVector(1110, "y", 12, [4, 33])
        self.__list_of_vectors2.add_a_vector(self.__va1)
        self.assertEqual(len(self.__list_of_vectors2.get_all_vectors()),2)
        self.__list_of_vectors2.add_a_vector(self.__va2)
        self.assertEqual(len(self.__list_of_vectors2.get_all_vectors()), 3)
        self.__list_of_vectors2.add_a_vector(self.__va3)
        self.assertEqual(len(self.__list_of_vectors2.get_all_vectors()), 4)
        self.__list_of_vectors2.add_a_vector(self.__va4)
        self.assertEqual(len(self.__list_of_vectors2.get_all_vectors()), 5)
        self.__list_of_vectors2.add_a_vector(self.__va5)
        self.assertEqual(len(self.__list_of_vectors2.get_all_vectors()), 6)
    def test_get_all_vectors(self):
        self.assertEqual(len(self.__result), 3)
        self.assertEqual(len(self.__result2), 1)
        self.assertEqual(len(self.__list_of_vectors3.get_all_vectors()), 1)
        self.assertEqual(len(self.__list_of_vectors4.get_all_vectors()), 3)
        self.assertEqual(len(self.__list_of_vectors5.get_all_vectors()), 2)

    def test_get_a_vector_at_an_index(self):
        self.assertRaises(IndexError, self.__list_of_vectors2.get_a_vector_at_an_index, -5)
        self.assertEqual(self.__list_of_vectors2.get_a_vector_at_an_index(0).get_name_id(),3)
        self.assertEqual(self.__list_of_vectors4.get_a_vector_at_an_index(1).get_colour(), "m")
        self.assertEqual(self.__list_of_vectors4.get_a_vector_at_an_index(1).get_name_id(),13)
        self.assertIsNotNone(self.__list_of_vectors5.get_a_vector_at_an_index(1))

    def test_update_a_vector(self):
        self.__list_of_vectors4.update_a_vector(1, "r", 2, [1])
        self.mylist = self.__list_of_vectors4.get_all_vectors()
        self.assertEqual(self.mylist[1].get_colour(), "r")
        self.assertEqual(self.mylist[1].get_vector_type(), 2)
        self.assertEqual(self.mylist[1].get_values().tolist(), [1])
        self.assertEqual(self.mylist[1].get_name_id(), 13)
        self.assertIsNotNone(self.mylist[1])

    def test_get_the_list_of_vector_with_minimum_elements(self):
        self.assertEqual(len(self.__list_of_vectors.get_the_list_of_vector_with_minimum_elements(4)), 1)
        self.assertRaises(IndexError, self.__list_of_vectors4.get_the_list_of_vector_with_minimum_elements, 47)
        self.assertRaises(IndexError, self.__list_of_vectors4.get_the_list_of_vector_with_minimum_elements, 25)
        self.assertEqual(len(self.__list_of_vectors2.get_the_list_of_vector_with_minimum_elements(433)), 1)
        self.assertEqual(len(self.__list_of_vectors2.get_the_list_of_vector_with_minimum_elements(0)), 0)

    def test_get_the_sum_of_all_vectors(self):

        self.assertEqual(self.__list_of_vs1.get_the_sum_of_all_vectors().get_values().tolist(),[2])
        self.assertEqual(self.__list_of_vs2.get_the_sum_of_all_vectors().get_values().tolist(), [6])
        self.assertEqual(self.__list_of_vs2.get_the_sum_of_all_vectors().get_name_id(),102)
        self.assertEqual(self.__list_of_vs2.get_the_sum_of_all_vectors().get_colour(),"r")
        self.assertEqual(self.__list_of_vs2.get_the_sum_of_all_vectors().get_vector_type(),5)

    def test_update_a_vector_by_name(self):
        self.__list_of_vectors5.update_a_vector_by_name(2, "r", 42, [1])
        ls=self.__list_of_vectors5.get_all_vectors()
        index=-1
        for vec in range(len(ls)):
            if ls[vec].get_name_id()==2:
                index=vec
                break
        self.assertEqual(self.__list_of_vectors5.get_a_vector_at_an_index(index).get_colour(),"r")
        self.assertEqual(self.__list_of_vectors5.get_a_vector_at_an_index(index).get_vector_type(),42)
        self.assertEqual(self.__list_of_vectors5.get_a_vector_at_an_index(index).get_values(),[1])
        self.assertEqual(self.__list_of_vectors5.get_a_vector_at_an_index(index).get_name_id(),2)

    def test_delete_a_vector_by_index(self):
        self.__list_of_vectors2.delete_a_vector_by_index(0)
        self.assertEqual(len(self.__list_of_vectors2.get_all_vectors()),0)
        self.assertRaises(IndexError,self.__list_of_vectors2.delete_a_vector_by_index,-9)
        self.assertRaises(IndexError,self.__list_of_vectors2.delete_a_vector_by_index,120)
        self.__list_of_vectors4.delete_a_vector_by_index(0)
        self.assertEqual(len(self.__list_of_vectors4.get_all_vectors()),2)
        self.assertRaises(IndexError, self.__list_of_vectors4.delete_a_vector_by_index, -120)

    def test_delete_a_vector_by_name(self):
        self.__list_of_vs4.delete_a_vector_by_name(109)
        self.assertEqual(len(self.__list_of_vs4.get_all_vectors()),1)
        self.assertRaises(ValueError,self.__list_of_vs4.delete_a_vector_by_name,2000)
        self.__list_of_vs3.delete_a_vector_by_name(104)
        self.assertEqual(len(self.__list_of_vs3.get_all_vectors()),0)
        self.assertRaises(ValueError,self.__list_of_vs3.delete_a_vector_by_name,5000)
    
if __name__ == "__main__":
    unittest.main()
