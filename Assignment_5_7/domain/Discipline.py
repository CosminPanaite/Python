import unittest

class Discipline:
    '''
    Class reffering to Discipline entity
    '''
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def getName(self):
        '''
        Returns the name of the discipline
        '''
        return self._name

    def getId(self):
        '''
        Returns the id of the discipline
        '''
        return self._id

    def setName(self, new_name):
        '''
        Sets the name of the discipline
        :param new_name: string
        :return:
        '''
        self._name = new_name

    def setId(self, new_id):
        '''
        Sets the id of the discipline
        :param new_id: integer
        :return:
        '''
        self._id = new_id

    def __str__(self):
        return "ID: " + str(self._id) + " || " + "Name: " + str(self._name)

class TestDiscipline(unittest.TestCase):
    '''
    TEST CLASS FOR DISCIPLINE ENTITY
    '''
    def setUp(self):
        self.discipline = Discipline(21, "Math")

    def tearDown(self):
        self.discipline = None

    def test(self):
        self.assertEqual(self.discipline.getName(), "Math")
        self.assertEqual(self.discipline.getId(), 21)
        self.discipline.setName("Fp")
        self.assertEqual(self.discipline.getName(), "Fp")