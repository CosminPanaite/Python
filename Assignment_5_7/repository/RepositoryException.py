class RepositoryException(Exception):
    '''
    Repository Errors Class
    '''
    def __init__(self, error):
        self._error = error

    def getError(self):
        return self._error