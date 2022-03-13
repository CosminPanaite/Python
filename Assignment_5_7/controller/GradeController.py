from Assignment_5_7.domain.Grade import Grade
from Assignment_5_7.controller.UndoController import *

class GradeController:
    '''
    Controller Class for Grades
    '''
    def __init__(self, validator, repository, undo_controller):
        self.__validator = validator
        self.__repository = repository
        self._undo_controller = undo_controller

    def addGrade(self, studentId, disciplineId, grade_value):
        grade = Grade(studentId, disciplineId, grade_value)
        self.__validator.validate(grade)
        self.__repository.addGrade(grade)

        undo = FunctionCall(self.deleteGrade, studentId, disciplineId, grade_value)
        redo = FunctionCall(self.addGrade, studentId, disciplineId, grade_value)
        operation = Operation(undo, redo)
        self._undo_controller.add(operation)

        return grade

    def deleteGrade(self, studentId, disciplineId, grade_value):
        return self.__repository.deleteGrade(studentId, disciplineId, grade_value)

    def deleteStudentGrades(self, studentId):
        return self.__repository.deleteStudentGrades(studentId)

    def deleteDisciplineGrades(self, disciplineId):
        return self.__repository.deleteDisciplineGrades(disciplineId)

    def getAllGrades(self):
        return self.__repository.getGrades()

    def enrolledStudents(self, disciplineId):
        return self.__repository.enrolledStudents(disciplineId)

    def averageGradeDiscipline(self, studentId, disciplineId):
        return self.__repository.averageGradeDiscipline(studentId, disciplineId)

    def aggregatedAverage(self, studentId):
        return self.__repository.aggregatedAverage(studentId)

    def averageGradeDisciplineAll(self, disciplineId):
        return self.__repository.averageGradeDisciplineAll(disciplineId)


