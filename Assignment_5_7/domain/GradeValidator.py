from Assignment_5_7.domain.Grade import Grade
from Assignment_5_7.domain.ValidatorException import ValidatorException

class GradeValidator:
    '''
    Validation class for Grades
    '''
    def validate(self, grade):
        '''
        :param grade: instance of Grade type
        :return: list of validation errors or an empty list if no error occure
        '''
        if isinstance(grade, Grade) == False:
            raise TypeError("Not a grade.")

        _errors = []

        try:
            int(grade.getStudentId())
        except:
            _errors.append("Student ID has to be integer.")

        try:
            int(grade.getDisciplineId())
        except:
            _errors.append("Discipline ID has to be an integer.")

        try:
            float(grade.getGradeValue())
            if float(grade.getGradeValue()) < 1.0 or float(grade.getGradeValue()) > 10.0:
                _errors.append("The grade value has to be between in [1, 10]. ")
        except:
            _errors.append("Grade value has to be float.")

        if len(_errors) != 0:
            raise ValidatorException(_errors)