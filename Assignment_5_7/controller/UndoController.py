class UndoController:
    '''
    Undo \ Redo Controller Class
    '''
    def __init__(self):
        self._operations = []
        self._index = -1
        self._duringUndo = False

    def add(self, operation):
        if self._duringUndo == True:
            return
        self._operations.append(operation)
        self._index = len(self._operations) - 1

    def undo(self):
        if self._index < 0:
            return False

        self._duringUndo = True
        self._operations[self._index].undo()
        self._duringUndo = False
        self._index -= 1
        return True

    def redo(self):
        if self._index >= len(self._operations) - 1:
            print("X")
            return False

        self._index += 1
        self._duringUndo = True
        self._operations[self._index].redo()
        self._duringUndo = False
        return True

class FunctionCall:
    def __init__(self, function, *params):
        self._function = function
        self._params = params

    def call(self):
        self._function(*self._params)

class CascadeOperation:
    def __init__(self):
        self._operations = []

    def add(self, operation):
        self._operations.append(operation)

    def undo(self):
        for op in self._operations:
            op.undo()

    def redo(self):
        for op in self._operations:
            op.redo()

class Operation:
    def __init__(self, undoFunction, redoFunction):
        self._undoFunction = undoFunction
        self._redoFunction = redoFunction

    def undo(self):
        self._undoFunction.call()

    def redo(self):
        self._redoFunction.call()