from Assignment_5_7.domain.Discipline import Discipline
from Assignment_5_7.controller.UndoController import *

class DisciplineController:
    '''
    Controller Class for Disciplines
    '''
    def __init__(self, validator, repository, undo_controller, grade_controller):
        self.__validator = validator
        self.__repository = repository
        self._undo_controller = undo_controller
        self._grade_controller = grade_controller

    def addDiscipline(self, disciplineId, disciplineName):
        discipline = Discipline(disciplineId, disciplineName)
        self.__validator.validate(discipline)
        self.__repository.addDiscipline(discipline)

        redo = FunctionCall(self.addDiscipline, disciplineId, disciplineName)
        undo = FunctionCall(self.deleteDiscipline, disciplineId)
        operation = Operation(undo, redo)
        self._undo_controller.add(operation)

        return discipline

    def deleteDiscipline(self, disciplineId):
        undo = FunctionCall(self.addDiscipline, disciplineId, self.__repository.getDisciplineNameById(disciplineId))
        redo = FunctionCall(self.deleteDiscipline, disciplineId)
        operation = Operation(undo, redo)
        cascade = CascadeOperation()
        cascade.add(operation)

        deleted = self._grade_controller.deleteDisciplineGrades(disciplineId)

        for grade in deleted:
            undo = FunctionCall(self._grade_controller.addGrade, grade.getStudentId(), grade.getDisciplineId(), grade.getGradeValue())
            redo = FunctionCall(self._grade_controller.deleteGrade, grade.getStudentId(), grade.getDisciplineId(), grade.getGradeValue())
            operation = Operation(undo, redo)
            cascade.add(operation)

        self._undo_controller.add(cascade)

        return self.__repository.deleteDiscipline(disciplineId)

    def updateDiscipline(self, disciplineId, new_name):
        undo = FunctionCall(self.updateDiscipline, disciplineId, self.__repository.getDisciplineNameById(disciplineId))
        redo = FunctionCall(self.updateDiscipline, disciplineId, new_name)
        operation = Operation(undo, redo)
        self._undo_controller.add(operation)

        return self.__repository.updateDiscipline(disciplineId, new_name)

    def searchDisciplineName(self, string):
        return self.__repository.searchDisciplineNameBased(string)

    def searchDisciplineId(self, id):
        return self.__repository.searchDisciplineIdBased(id)

    def getDisciplineNameById(self, id):
        return self.__repository.getDisciplineNameById(id)

    def getAllDisciplines(self):
        return self.__repository.getDisciplines()

    def isDiscIdUsed(self, id):
        return self.__repository.isIdUsed(id)