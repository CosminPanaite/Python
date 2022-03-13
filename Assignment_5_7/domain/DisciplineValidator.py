from Assignment_5_7.domain.Discipline import Discipline
from Assignment_5_7.domain.ValidatorException import ValidatorException

class DisciplineValidator:
    '''
    Validation class for Disciplines
    '''
    def validate(self, discipline):
        '''
        :param discipline: instance of Discipline type
        :return: list of validation errors or an empty list if no error occure
        '''
        if isinstance(discipline, Discipline) == False:
            raise TypeError("Not a discipline.")

        _errors = []

        try:
            int(discipline.getId())
        except:
            _errors.append("Discipline ID has to be an integer.")

        if len(discipline.getName()) == 0:
            _errors.append("Discipline name cannot be empty.")

        if len(_errors) != 0:
            raise ValidatorException(_errors)