class MyPoint:
    def __init__(self, coord_x, coord_y, colour):
        '''
        a class for
        :param coord_x:
        :param coord_y:
        :param colour:
        '''
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.colour = colour

    def getCoordinate_X(self):
        '''
        getter method
        return the coordinate x of a point
        '''
        return self.coord_x

    def getCoordinate_Y(self):
        '''
        getter method
        return the coordinate y of a point
        '''
        return self.coord_y

    def getColour(self):
        '''
        getter method
        return the colour of a point
        '''
        return self.colour

    def set_coord_x(self, new_coord_x):
        self.coord_x = new_coord_x  # set a new coordinate for x

    def set_coord_y(self, new_coord_y):
        self.coord_y = new_coord_y

    def set_Colour(self, new_colour):
        self.colour = new_colour

    def __str__(self):
        '''

        :return:
        '''
        return f"Point ({self.coord_x},{self.coord_y}) is of colour {self.colour}"
