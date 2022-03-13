import unittest
from Domain.MyVector import MyVector
from Controller.ctrl import VectorController
from Domain.Validator import VectorValidator
from Repository.repo import VectorRepository


class ControllerTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__list_validator = VectorValidator()

        self.__list_repo=VectorRepository(self.__list_validator)
        self.list_ctrl_v=VectorController(self.__list_repo,self.__list_validator)
        self.list_ctrl_v = VectorController(self.__list_repo, self.__list_validator)
        self.__list_repo2 = VectorRepository(self.__list_validator)
        self.list_ctrl_v2 = VectorController(self.__list_repo2, self.__list_validator)
        self.list_ctrl_v2.ctrl_add_a_vector(45, "r", 20, [25])
        self.__list_repo3 = VectorRepository(self.__list_validator)
        self.list_ctrl_v3 = VectorController(self.__list_repo3, self.__list_validator)
        self.list_ctrl_v3.ctrl_add_a_vector(46, "r", 20, [25,30])
        self.list_ctrl_v3.ctrl_add_a_vector(47, "y", 30, [40,25])
        self.__list_repo4 = VectorRepository(self.__list_validator)
        self.list_ctrl_v4 = VectorController(self.__list_repo4, self.__list_validator)
        self.list_ctrl_v4.ctrl_add_a_vector(48, "y", 30, [40, 25])
        self.__list_repo5 = VectorRepository(self.__list_validator)
        self.list_ctrl_v5 = VectorController(self.__list_repo5, self.__list_validator)
        self.list_ctrl_v5.ctrl_add_a_vector(50, "y", 30, [40, 25])
        self.list_ctrl_v5.ctrl_add_a_vector(51, "r", 30, [40, 5])
        self.list_ctrl_v5.ctrl_add_a_vector(52, "g", 30, [40, 15])
        self.list_ctrl_v5.ctrl_add_a_vector(53, "y", 30, [40, 35])
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_ctrl_add_a_vector(self):
        self.list_ctrl_v.ctrl_add_a_vector(2500,"r",20,[25])
        self.assertEqual(len(self.list_ctrl_v.ctrl_get_all_vectors()),1)
        self.list_ctrl_v.ctrl_add_a_vector(2501, "r", 20, [25])
        self.assertEqual(len(self.list_ctrl_v.ctrl_get_all_vectors()), 2)
        self.list_ctrl_v.ctrl_add_a_vector(2502, "r", 20, [25])
        self.assertEqual(len(self.list_ctrl_v.ctrl_get_all_vectors()), 3)
        self.list_ctrl_v.ctrl_add_a_vector(2503, "r", 20, [25])
        self.assertEqual(len(self.list_ctrl_v.ctrl_get_all_vectors()), 4)
        self.list_ctrl_v.ctrl_add_a_vector(2504, "r", 20, [25])
        self.assertEqual(len(self.list_ctrl_v.ctrl_get_all_vectors()), 5)
    def test_ctrl_get_all_vectors(self):
        self.assertEqual(len(self.list_ctrl_v2.ctrl_get_all_vectors()),1)
        self.assertEqual(len(self.list_ctrl_v3.ctrl_get_all_vectors()),2)
        self.list_ctrl_v3.ctrl_add_a_vector(3500, "r", 20, [25])
        self.assertEqual(len(self.list_ctrl_v3.ctrl_get_all_vectors()), 3)
        self.list_ctrl_v3.ctrl_add_a_vector(3501, "r", 20, [25])
        self.assertEqual(len(self.list_ctrl_v3.ctrl_get_all_vectors()), 4)
        self.list_ctrl_v3.ctrl_add_a_vector(3502, "r", 20, [25])
        self.assertEqual(len(self.list_ctrl_v3.ctrl_get_all_vectors()), 5)
    def test_ctrl_get_a_vector_at_an_index(self):
        self.assertEqual(self.list_ctrl_v4.ctrl_get_a_vector_at_an_index(0).get_colour(),"y")
        self.assertEqual(self.list_ctrl_v4.ctrl_get_a_vector_at_an_index(0).get_vector_type(), 30)
        self.assertEqual(self.list_ctrl_v4.ctrl_get_a_vector_at_an_index(0).get_values().tolist(), [40,25])
        self.assertEqual(self.list_ctrl_v4.ctrl_get_a_vector_at_an_index(0).get_name_id(),48)
        self.assertEqual(self.list_ctrl_v3.ctrl_get_a_vector_at_an_index(1).get_name_id(),47)
    def test_ctrl_update_a_vector(self):
        self.list_ctrl_v4.ctrl_update_a_vector( 0, "g" , 255, [30,40,50,60,70])
        self.assertEqual(self.list_ctrl_v4.ctrl_get_a_vector_at_an_index(0).get_colour(), "g")
        self.assertEqual(self.list_ctrl_v4.ctrl_get_a_vector_at_an_index(0).get_vector_type(), 255)
        self.assertEqual(self.list_ctrl_v4.ctrl_get_a_vector_at_an_index(0).get_values().tolist(), [30, 40 , 50 ,60, 70])
        self.assertEqual(self.list_ctrl_v4.ctrl_get_a_vector_at_an_index(0).get_name_id(), 48)
    def test_ctrl_update_a_vector_by_name(self):
        self.list_ctrl_v5.ctrl_update_a_vector_by_name( 51, "g",3000, [4000,3000,2000])
        ls = self.list_ctrl_v5.ctrl_get_all_vectors()
        index1 = -1
        for vec in range(len(ls)):
            if ls[vec].get_name_id() == 51:
                index1 = vec
                break
        self.assertEqual(self.list_ctrl_v5.ctrl_get_a_vector_at_an_index(index1).get_colour(), "g")
        self.assertEqual(self.list_ctrl_v5.ctrl_get_a_vector_at_an_index(index1).get_vector_type(), 3000)
        self.assertEqual(self.list_ctrl_v5.ctrl_get_a_vector_at_an_index(index1).get_values().tolist(), [4000,3000,2000])
        self.assertEqual(self.list_ctrl_v5.ctrl_get_a_vector_at_an_index(index1).get_name_id(), 51)
    def test_ctrl_delete_a_vector_by_index(self):
        self.list_ctrl_v5.ctrl_delete_a_vector_by_index(0)
        self.assertEqual(len(self.list_ctrl_v5.ctrl_get_all_vectors()),3 )
        self.list_ctrl_v5.ctrl_delete_a_vector_by_index(0)
        self.assertEqual(len(self.list_ctrl_v5.ctrl_get_all_vectors()), 2)
        self.list_ctrl_v5.ctrl_delete_a_vector_by_index(0)
        self.assertEqual(len(self.list_ctrl_v5.ctrl_get_all_vectors()), 1)
        self.list_ctrl_v5.ctrl_delete_a_vector_by_index(0)
        self.assertEqual(len(self.list_ctrl_v5.ctrl_get_all_vectors()), 0)
        self.assertRaises(IndexError,self.list_ctrl_v5.ctrl_delete_a_vector_by_index,-50)
    def test_ctrl_delete_a_vector_by_name(self):
        self.list_ctrl_v5.ctrl_delete_a_vector_by_name( 50)
        self.assertEqual(len(self.list_ctrl_v5.ctrl_get_all_vectors()), 3)
        self.list_ctrl_v5.ctrl_delete_a_vector_by_name(51)
        self.assertEqual(len(self.list_ctrl_v5.ctrl_get_all_vectors()), 2)
        self.list_ctrl_v5.ctrl_delete_a_vector_by_name(52)
        self.assertEqual(len(self.list_ctrl_v5.ctrl_get_all_vectors()), 1)
        self.list_ctrl_v5.ctrl_delete_a_vector_by_name(53)
        self.assertEqual(len(self.list_ctrl_v5.ctrl_get_all_vectors()), 0)
        self.assertRaises(ValueError,self.list_ctrl_v5.ctrl_delete_a_vector_by_name,99)
    def test_ctrl_get_the_list_of_vector_with_minimum_elements(self):

        self.assertEqual(len(self.list_ctrl_v5.ctrl_get_the_list_of_vector_with_minimum_elements(22)),2)
        self.assertEqual(len(self.list_ctrl_v5.ctrl_get_the_list_of_vector_with_minimum_elements(100)), 2)
        self.assertEqual(len(self.list_ctrl_v5.ctrl_get_the_list_of_vector_with_minimum_elements(0)), 0)
        self.assertEqual(len(self.list_ctrl_v3.ctrl_get_the_list_of_vector_with_minimum_elements(22)),0)
        self.assertEqual(len(self.list_ctrl_v2.ctrl_get_the_list_of_vector_with_minimum_elements(2222)),1)
    def test_ctrl_get_the_sum_of_all_vectors(self):
        self.assertEqual(self.list_ctrl_v2.ctrl_get_the_sum_of_all_vectors().get_values().tolist(),[25])
        self.assertEqual(self.list_ctrl_v3.ctrl_get_the_sum_of_all_vectors().get_values().tolist(),[65,55])
        self.assertEqual(self.list_ctrl_v3.ctrl_get_the_sum_of_all_vectors().get_name_id(), 46)
        self.assertEqual(self.list_ctrl_v3.ctrl_get_the_sum_of_all_vectors().get_colour(), "r")
        self.assertEqual(self.list_ctrl_v3.ctrl_get_the_sum_of_all_vectors().get_vector_type(), 20)
if __name__ == "__main__":
    unittest.main()
