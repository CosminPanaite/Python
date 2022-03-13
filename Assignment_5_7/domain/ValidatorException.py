class ValidatorException(Exception):
    '''
    Validation Errors Class
    '''
    def __init__(self, error = ["Validation error!\n"]):
        self._errorList = error

    def getErrors(self):
        return self._errorList

    def __str__(self):
        errorList= self.getErrors()
        result = " "
        for error in errorList:
            result += error
            result += "\n"
        return result
