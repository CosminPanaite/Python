from Assignment_5_7.domain.Student import Student
from Assignment_5_7.repository.RepositoryException import RepositoryException
import unittest

class StudentRepository:
    '''
    Repository Class for Students
    '''
    def __init__(self):
        self._studentList = []

    def getStudents(self):
        return self._studentList

    def isIdUsed(self, studentId):
        '''
        Checks if the id is already in use
        :param student: Student type
        :return: True if the id is already in use, False if it is not
        '''
        for s in self._studentList:
            if int(s.getId()) == int(studentId):
                return True
        return False

    def  addStudent(self, student):
        '''
        Stores a student in the repository
        :param student: Student type
        :return: True if the student was added
        '''
        if self.isIdUsed(student.getId()):
            raise RepositoryException("Student ID already used.")
        self._studentList.append(student)
        return True

    def deleteStudent(self, studentId):
        '''
        Deletes the student with the given id
        :param studentId: int - the id of the student that has to be deleted
        :return: True if the student was deleted, False otherwise
        '''
        if self.isIdUsed(studentId) == False:
            raise RepositoryException("No student with given ID.")
        for student in self._studentList:
            if int(studentId) == int(student.getId()):
                self._studentList.remove(student)
                return True
        return False

    def updateStudent(self, studentId, new_name):
        '''
        :param studentId: int - the id of the student that has to be updated
        :param new_name: string - the new name of the student
        :return: True if the student was updated, False otherwise
        '''
        if self.isIdUsed(studentId) == False:
            raise RepositoryException("No student with given ID.")
        for student in self._studentList:
            if int(studentId) == int(student.getId()):
                student.setName(new_name)
                return True
        return False

    def searchStudentNameBased(self, string):
        '''
        Searches for students based on name
        :param string: string
        :return: Returns False if there is no student fround with partial string matching
                 Returns the list of mathcing students if there are any
        '''
        foundList = []
        for student in self._studentList:
            if string.lower() in student.getName().lower():
                foundList.append(student)
        if len(foundList) == 0:
            return False
        return foundList

    def searchStudentIdBased(self, id):
        '''
        Searches for students based on id
        :param id: int
        :return: Returns False if there was no id match
                 Returns the list of mathcing students if there are any
        '''
        foundList = []
        for student in self._studentList:
            if str(id) in str(student.getId()):
                foundList.append(student)
        if len(foundList) == 0:
            return False
        return foundList

    def getStudentNameById(self, id):
        '''
        :param id: int
        :return: name of the student with given id
        '''
        for student in self._studentList:
            if int(id) == int(student.getId()):
                return student.getName()

    def __str__(self):
        result = " "
        for student in self._studentList:
            result += str(student)
            result += "\n"
        return result

class TestStudentRepo(unittest.TestCase):
    '''
    TEST CLASS FOR STUDENT REPOSITORY
    '''
    def setUp(self):
        self.studentList = StudentRepository()

    def tearDown(self):
        self.studentList = None

    def test(self):
        self.assertTrue(self.studentList.addStudent(Student(12, "Copa Malina")))
        self.assertTrue(self.studentList.addStudent(Student(17, "Tao Crig")))
        self.assertFalse(self.studentList.isIdUsed(55))
        self.assertTrue(self.studentList.deleteStudent(12))
        self.assertTrue(self.studentList.updateStudent(17, "Marw Ayno"))
        self.assertEqual(self.studentList.getStudentNameById(17), "Marw Ayno")
        self.assertNotEqual(self.studentList.searchStudentNameBased("ma"), None)
        self.assertNotEqual(self.studentList.searchStudentIdBased(17), None)
