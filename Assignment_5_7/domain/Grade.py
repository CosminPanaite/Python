import unittest

class Grade:
    '''
    Class reffering to Grade entity
    '''
    def __init__(self, student_id, discipline_id, grade):
        self._studentId = student_id
        self._disciplineId = discipline_id
        self._value = grade

    def getStudentId(self):
        '''
        Returns the id of the student
        :return:
        '''
        return self._studentId

    def getDisciplineId(self):
        '''
        Returns the id of the discipline
        :return:
        '''
        return self._disciplineId

    def getGradeValue(self):
        '''
        Returns the value of the grade
        :return:
        '''
        return self._value

    def setGradeValue(self, new_value):
        '''
        Sets the value of the grade
        :param new_value: float
        :return:
        '''
        self._value = new_value

class TestGrade(unittest.TestCase):
    '''
    TEST CLASS FOR GRADE ENTITY
    '''
    def setUp(self):
        self.grade = Grade(23, 14, 9)

    def tearDown(self):
        self.grade = None

    def test(self):
        self.assertEqual(self.grade.getStudentId(), 23)
        self.assertEqual(self.grade.getDisciplineId(), 14)
        self.assertEqual(self.grade.getGradeValue(), 9)
        self.grade.setGradeValue(10)
        self.assertEqual(self.grade.getGradeValue(), 10)