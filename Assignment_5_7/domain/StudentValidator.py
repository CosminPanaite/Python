from Assignment_5_7.domain.Student import Student
from Assignment_5_7.domain.ValidatorException import ValidatorException

class StudentValidator:
    '''
    Validation class for Students
    '''
    def validate(self, student):
        '''
        :param student: instance of Student type
        :return: list of validation errors or an empty list if no error occure
        '''
        if isinstance(student, Student) == False:
            raise TypeError ("Not a student")

        _errors = []

        try:
            int(student.getId())
        except:
            _errors.append("Student ID has to be integer.")

        if len(student.getName()) == 0:
            _errors.append("Student name cannot be empty.")

        if len(_errors) != 0:
            raise ValidatorException(_errors)