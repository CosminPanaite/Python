import numpy as np
import unittest
from Domain.MyVector import MyVector


class TestMyVector(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__v = MyVector(2, "m", 22, [40, 53, 41])
        self.__v2 = MyVector(1, "m", 4, [22, 33, 2])
        self.__v3 = MyVector(5, "r", 10, [30, 40, 20, 50])
        self.__v4 = MyVector(6, "m", 10, [30, 40, 20, 50])
        self.__v5 = MyVector(7, "g", 15, [2])
        self.__v6 = MyVector(41, "y", 4, [5])
        self.__v7 = MyVector(43, "y", 4, [])
        self.__v8 = MyVector(44, "y", 4, [10,20,30])
        self.__v9 = MyVector(101, "m", 445, [])
        self.__v10 = MyVector(100, "n", 3 ,[])

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_create_vector(self):

        self.assertEqual(self.__v.get_vector_type(), 22)
        self.assertEqual(self.__v2.get_vector_type(), 4)
        self.assertEqual(self.__v3.get_vector_type(), 10)
        self.assertEqual(self.__v4.get_vector_type(), 10)
        self.assertEqual(self.__v.get_name_id(), 2)
        self.assertEqual(self.__v2.get_name_id(), 1)
        self.assertEqual(self.__v3.get_name_id(), 5)
        self.__v.set_name_id(30)
        self.assertEqual(self.__v.get_name_id(), 30)
        self.assertEqual(self.__v6.get_values().tolist(),[5])
        self.assertEqual(self.__v5.get_values().tolist(),[2])
        self.assertEqual(self.__v4.get_values().tolist(),[30, 40, 20, 50])
    def test_add_a_scalar(self):
        self.assertEqual(self.__v5.add_a_scalar(5).tolist(),[7])
        self.assertEqual(self.__v.add_a_scalar(2).tolist(), [42,55,43])
        self.assertEqual(self.__v7.add_a_scalar(100).tolist(),[])
        self.assertEqual(self.__v8.add_a_scalar(1).tolist(),[11,21,31])
        self.assertEqual(self.__v2.add_a_scalar(1000).tolist(),[1022, 1033, 1002])
    def test_add_two_vectors(self):
        self.assertEqual(self.__v.add_two_vectors(self.__v2).tolist(),[62,86,43])
        self.assertEqual(self.__v2.add_two_vectors(self.__v).tolist(),[84,119,45])
        self.assertEqual(self.__v5.add_two_vectors(self.__v6).tolist(),[7])
        self.assertEqual(self.__v5.add_two_vectors(self.__v6).tolist(),[12])
        self.assertEqual(self.__v7.add_two_vectors(self.__v9).tolist(),[])
    def test_subtract_two_vectors(self):
        self.assertEqual(self.__v.subtract_two_vectors(self.__v2).tolist(),[18, 20, 39])
        self.assertEqual(self.__v2.subtract_two_vectors(self.__v).tolist(), [4, 13, -37])
        self.assertEqual(self.__v5.subtract_two_vectors(self.__v6).tolist(), [-3])
        self.assertEqual(self.__v5.subtract_two_vectors(self.__v6).tolist(), [-8])
        self.assertEqual(self.__v7.subtract_two_vectors(self.__v9).tolist(), [])
    def test_multiplication_of_vectors(self):
        self.assertEqual(self.__v.multiplication_of_vectors(self.__v2), 2711)
        self.assertEqual(self.__v2.multiplication_of_vectors(self.__v), 2711)
        self.assertEqual(self.__v5.multiplication_of_vectors(self.__v6), 10)
        self.assertEqual(self.__v5.multiplication_of_vectors(self.__v6), 10)
        self.assertEqual(self.__v7.multiplication_of_vectors(self.__v9), 0)
    def test_sum_of_array(self):
        self.assertEqual(self.__v.sum_of_array(),134)
        self.assertEqual(self.__v2.sum_of_array(),57)
        self.assertEqual(self.__v3.sum_of_array(), 140)
        self.assertEqual(self.__v4.sum_of_array(), 140)
        self.assertEqual(self.__v5.sum_of_array(), 2)
    def test_maxim_of_array(self):
        self.assertEqual(self.__v.maxim_of_array(),53)
        self.assertRaises(IndexError,self.__v10.maxim_of_array)
        self.assertEqual(self.__v2.maxim_of_array(),33)
        self.assertEqual(self.__v3.maxim_of_array(),50)
        self.assertEqual(self.__v6.maxim_of_array(), 5)

    def test_minim_of_array(self):
        self.assertEqual(self.__v.minim_of_array(),40)
        self.assertRaises(IndexError,self.__v10.minim_of_array)
        self.assertEqual(self.__v2.minim_of_array(),2)
        self.assertEqual(self.__v3.minim_of_array(),20)
        self.assertEqual(self.__v6.minim_of_array(), 5)
    def test_average_of_array(self):
        self.assertEqual(self.__v.average_of_array(),44.666666666666664)
        self.assertEqual(self.__v2.average_of_array(), 19.0)
        self.assertEqual(self.__v3.average_of_array(), 35.0)
        self.assertEqual(self.__v4.average_of_array(), 35.0)
        self.assertRaises(IndexError,self.__v10.average_of_array)
    def test_product_of_array(self):
        self.assertEqual(self.__v.product_of_array(),86920)
        self.assertEqual(self.__v2.product_of_array(),1452)
        self.assertEqual(self.__v3.product_of_array(),1200000)
        self.assertEqual(self.__v5.product_of_array(),2)
        self.assertEqual(self.__v7.product_of_array(),0)

if __name__ == "__main__":
    unittest.main()
