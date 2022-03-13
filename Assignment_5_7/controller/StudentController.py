from Assignment_5_7.domain.Student import Student
from Assignment_5_7.domain.Grade import Grade
from Assignment_5_7.controller.UndoController import *

class StudentController:
    '''
    Controller Class for Students
    '''
    def __init__(self, validator, repository, undo_controller, grade_controller):
        self.__validator = validator
        self.__repository = repository
        self._undo_controller = undo_controller
        self._grade_controller = grade_controller

    def addStudent(self, studentId, studentName):
        student = Student(studentId, studentName)
        self.__validator.validate(student)
        self.__repository.addStudent(student)

        redo = FunctionCall(self.addStudent, studentId, studentName)
        undo = FunctionCall(self.deleteStudent, studentId)
        operation = Operation(undo, redo)
        self._undo_controller.add(operation)

        return student

    def deleteStudent(self, studentId):
        undo = FunctionCall(self.addStudent, studentId, self.__repository.getStudentNameById(studentId))
        redo = FunctionCall(self.deleteStudent, studentId)
        operation = Operation(undo, redo)
        cascade = CascadeOperation()
        cascade.add(operation)

        deleted = self._grade_controller.deleteStudentGrades(studentId)

        for grade in deleted:
            undo = FunctionCall(self._grade_controller.addGrade, grade.getStudentId(), grade.getDisciplineId(), grade.getGradeValue())
            redo = FunctionCall(self._grade_controller.deleteGrade, grade.getStudentId(), grade.getDisciplineId(), grade.getGradeValue())
            operation = Operation(undo, redo)
            cascade.add(operation)

        self._undo_controller.add(cascade)

        return self.__repository.deleteStudent(studentId)

    def updateStudent(self, studentId, new_name):
        undo = FunctionCall(self.updateStudent, studentId, self.__repository.getStudentNameById(studentId))
        redo = FunctionCall(self.updateStudent, studentId, new_name)
        operation = Operation(undo, redo)
        self._undo_controller.add(operation)

        return self.__repository.updateStudent(studentId, new_name)

    def searchStudentName(self, string):
        return self.__repository.searchStudentNameBased(string)

    def searchStudentId(self, id):
        return self.__repository.searchStudentIdBased(id)

    def getStudentNameById(self, id):
        return self.__repository.getStudentNameById(id)

    def getAllStudents(self):
        return self.__repository.getStudents()

    def isStudIdUsed(self, id):
        return self.__repository.isIdUsed(id)