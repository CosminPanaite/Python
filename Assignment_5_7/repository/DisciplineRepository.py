from Assignment_5_7.domain.Discipline import Discipline
from Assignment_5_7.repository.RepositoryException import RepositoryException
import unittest

class DisciplineRepository:
    '''
    Repository class for disciplines
    '''
    def __init__(self):
        self._disciplineList = []

    def getDisciplines(self):
        return self._disciplineList

    def isIdUsed(self, disciplineId):
        '''
        Checks if the id is already in use
        :param discipline: Discipline type
        :return: True if the id is already in use, False if it is not
        '''
        for s in self._disciplineList:
            if int(s.getId()) == int(disciplineId):
                return True
        return False

    def addDiscipline(self, discipline):
        '''
        Stores a discipline in the repository
        :param discipline: Discipline type
        :return: True if the discipline was added
        '''
        if self.isIdUsed(discipline.getId()):
            raise RepositoryException("Discipline ID already used.")
        self._disciplineList.append(discipline)
        return True

    def deleteDiscipline(self, disciplineId):
        '''
        Deletes the discipline with the given id
        :param disciplineId: int - the id of the discipline that has to be deleted
        :return: True if the discipline was deleted, False otherwise
        '''
        if self.isIdUsed(disciplineId) == False:
            raise RepositoryException("No discipline with given ID.")
        for discipline in self._disciplineList:
            if int(disciplineId) == int(discipline.getId()):
                self._disciplineList.remove(discipline)
                return True
        return False

    def updateDiscipline(self, disciplineId, new_name):
        '''
        :param disciplineId: int - the id of the discipline that has to be updated
        :param new_name: string - the new name of the discipline
        :return: True if the discipline was updated, False otherwise
        '''
        if self.isIdUsed(disciplineId) == False:
            raise RepositoryException("No discipline with given ID.")
        for discipline in self._disciplineList:
            if int(disciplineId) == int(discipline.getId()):
                discipline.setName(new_name)
                return True
        return False

    def searchDisciplineNameBased(self, string):
        '''
        Searches for disciplines based on name
        :param string: string
        :return: Returns False if there is no discipline fround with partial string matching
                 Returns the list of mathcing disciplines if there are any
        '''
        foundList = []
        for discipline in self._disciplineList:
            if string.lower() in discipline.getName().lower():
                foundList.append(discipline)
        if len(foundList) == 0:
            return False
        return foundList

    def searchDisciplineIdBased(self, id):
        '''
        Searches for disciplines based on id
        :param id: int
        :return: Returns False if there was no id match
                 Returns the list of mathcing disciplines if there are any
        '''
        foundList = []
        for discipline in self._disciplineList:
            if str(id) in str(discipline.getId()):
                foundList.append(discipline)
        if len(foundList) == 0:
            return False
        return foundList

    def getDisciplineNameById(self, id):
        '''
        :param id: int
        :return: name of the discipline with given id
        '''
        for discipline in self._disciplineList:
            if int(id) == int(discipline.getId()):
                return discipline.getName()

class TestDisciplineRepo(unittest.TestCase):
    '''
    TEST CLASS FOR DISCIPLINE REPOSITORY
    '''
    def setUp(self):
        self.disciplineList = DisciplineRepository()

    def tearDown(self):
        self.disciplineList = None

    def test(self):
        self.assertTrue(self.disciplineList.addDiscipline(Discipline(19, "Math")))
        self.assertTrue(self.disciplineList.addDiscipline(Discipline(17, "English")))
        self.assertFalse(self.disciplineList.isIdUsed(55))
        self.assertTrue(self.disciplineList.deleteDiscipline(19))
        self.assertTrue(self.disciplineList.updateDiscipline(17, "Chinese"))
        self.assertEqual(self.disciplineList.getDisciplineNameById(17), "Chinese")
        self.assertNotEqual(self.disciplineList.searchDisciplineNameBased("ne"), None)
        self.assertNotEqual(self.disciplineList.searchDisciplineIdBased(17), None)
