import unittest

class Student:
    '''
    Class reffering to Student entity
    '''
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def getName(self):
        '''
        Returns the name of the student
        '''
        return self._name

    def getId(self):
        '''
        Returns the id of the student
        '''
        return self._id

    def setName(self, new_name):
        '''
        Sets the name of the studennt
        :param new_name: string
        :return:
        '''
        self._name = new_name

    def setId(self, new_id):
        '''
        Sets the id of the student
        :param new_id: integer
        :return:
        '''
        self._id = new_id

    def __str__(self):
        return "ID: " + str(self._id) + " || " + "Name: " + str(self._name)

class TestStudent(unittest.TestCase):
    '''
    TEST CLASS FOR STUDENT ENTITY
    '''
    def setUp(self):
        self.student = Student(23, "Cleo")

    def tearDown(self):
        self.student = None

    def test(self):
        self.assertEqual(self.student.getName(), "Cleo")
        self.assertEqual(self.student.getId(), 23)
        self.student.setName("Andy")
        self.assertEqual(self.student.getName(), "Andy")