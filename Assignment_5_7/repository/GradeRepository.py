from Assignment_5_7.domain.Grade import Grade
from Assignment_5_7.repository.RepositoryException import RepositoryException
import unittest

class GradeRepository:
    '''
    Repository Class for Grades
    '''
    def __init__(self):
        self._gradesList = []

    def getGrades(self):
        return self._gradesList

    def addGrade(self, grade):
        '''
        Stores a grade in the grade repository
        :param grade: Grade type
        :return: True if the Grade was added
        '''
        self._gradesList.append(grade)
        return True

    def deleteGrade(self, studentId, disciplineId, grade_value):
        '''
        Reverse function of addGrade for undo
        :param studentId:
        :param disciplineId:
        :param grade_value:
        :return:
        '''
        for grade in reversed(self._gradesList):
            if int(studentId) == int(grade.getStudentId()) and int(disciplineId) == int(grade.getDisciplineId()) and int(grade_value) == int(grade.getGradeValue()):
                self._gradesList.remove(grade)
                return True

    def deleteStudentGrades(self, studentID):
        '''
        Removes all the grades of a student that was deleted
        :param studentID: int
        :return: the list of deleted grades
        '''
        deleted = []
        for grade in self._gradesList:
            if int(studentID) == int(grade.getStudentId()):
                deleted.append(grade)
                self._gradesList.remove(grade)
        return deleted

    def deleteDisciplineGrades(self, disciplineID):
        '''
        Removes all the grades from a discipline that was deleted
        :param disciplineID: int
        :return:
        '''
        deleted = []
        for grade in self._gradesList:
            if int(disciplineID) == int(grade.getDisciplineId()):
                deleted.append(grade)
                self._gradesList.remove(grade)
        return deleted

    def enrolledStudents(self, disciplineID):
        '''
        :param disciplineID: int
        :return: the list of the ids of the students enrolled
        '''
        enrolledList = []
        for grade in self._gradesList:
            if int(disciplineID) == int(grade.getDisciplineId()):
                enrolledList.append(grade.getStudentId())
        if len(enrolledList) == 0:
            return False
        else:
            return (enrolledList)

    def averageGradeDiscipline(self, studentID, disciplineID):
        '''
        :param studentID: int
        :param disciplineID: int
        :return: average grade for a student at a discipline
        '''
        total = 0
        count = 0
        for grade in self._gradesList:
            if int(studentID) == int(grade.getStudentId()) and int(disciplineID) == int(grade.getDisciplineId()):
                total += int(grade.getGradeValue())
                count += 1
        if count != 0 :
            return total / count
        return False

    def getDisciplineIdsList(self):
        '''
        Returns all the discipline ids where there are grades
        :return:
        '''
        DidsList = []
        for grade in self._gradesList:
            if grade.getDisciplineId() not in DidsList:
                DidsList.append(grade.getDisciplineId())
        return DidsList

    def getStudentIdsList(self):
        '''
        Returns all the student ids that have at least a grade
        :return:
        '''
        SidsList = []
        for grade in self._gradesList:
            if grade.getStudentId() not in SidsList:
                SidsList.append(grade.getStudentId())
        return SidsList

    def  aggregatedAverage(self, studentId):
        '''
        :param studentID: int
        :return: aggregated average for given student
        '''
        DidsList = self.getDisciplineIdsList()
        total = 0
        count = 0
        for did in DidsList:
            avg = self.averageGradeDiscipline(studentId, did)
            if avg is not False:
                total += avg
                count += 1
        if count != 0 :
            return total / count
        return False

    def averageGradeDisciplineAll(self, disciplineId):
        '''
        :param disciplineID:
        :return: average grade received by all students enrolled at that discipline
        '''
        total = 0
        count = 0
        for grade in self._gradesList:
            if int(disciplineId) == int(grade.getDisciplineId()):
                total += int(grade.getGradeValue())
                count += 1
        if  count != 0:
            return total / count
        else:
            return False

class TestGradeRepo(unittest.TestCase):
    '''
    TEST CLASS FOR GRADE REPOSITORY
    '''
    def setUp(self):
        self.gradeList = GradeRepository()

    def tearDown(self):
        self.gradeList = None

    def test(self):
        self.assertTrue(self.gradeList.addGrade(Grade(12, 19, 7)))
        self.assertTrue(self.gradeList.addGrade(Grade(12, 19, 3)))
        self.assertTrue(self.gradeList.addGrade(Grade(45, 96, 4)))
        self.assertTrue(self.gradeList.addGrade(Grade(12, 14, 6)))
        self.assertTrue(self.gradeList.addGrade(Grade(31, 14, 4)))
        self.assertFalse(self.gradeList.enrolledStudents(88))
        self.assertEqual(self.gradeList.averageGradeDiscipline(12, 19), 5)
        self.assertEqual(self.gradeList.aggregatedAverage(12), 5.5)
        self.assertEqual(self.gradeList.averageGradeDisciplineAll(14), 5)