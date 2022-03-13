from Domain.my_point import MyPoint
from copy import deepcopy


class PointRepository:

    def __init__(self):
        self.points_storage = []  # an empty list in which I store the points

    def add_point_to_the_repository(self, coord_x, coord_y, colour):
        '''
        adds a point to the repository
        :param coord_x:
        :param coord_y:
        :param _colour:
        :return:
        '''
        if colour not in ["red", "green", "blue", "yellow", "magenta"]:
            raise ValueError("The colour of the point should be in the list ['red','green','blue','yellow','magenta']")
        point = MyPoint(coord_x, coord_y, colour)
        self.points_storage.append(point)

    def get_a_point_at_a_given_index(self, given_index):
        '''
        gets a point at a given index
        :param given_index:
        :return:
        '''
        if given_index < 0 or given_index >= len(self.points_storage):
            raise IndexError("The index is out of range!")
        return self.points_storage[given_index]

    def get_all_points_of_a_given_colour(self, given_colour):
        '''

        :param given_colour:
        :return:
        '''

        if given_colour not in ["red", "green", "blue", "yellow", "magenta"]:
            raise ValueError("The colour of the point should be in the list ['red','green','blue','yellow','magenta']")
        list_of_points = self.get_all_points()
        return [point.__str__() for point in list_of_points if point.colour == given_colour]
        # a list comprehension where all points are of a certain colour

    def update_a_point_at_a_given_index(self, given_index, new_coord_x, new_coord_y, new_colour):
        '''

        :param given_index:
        :param new_coord_x:
        :param new_coord_y:
        :param new_colour:
        :return:
        '''
        if given_index < 0 or given_index >= len(self.points_storage):
            raise IndexError("The index is out of range!")
        if new_colour not in ["red", "green", "blue", "yellow", "magenta"]:
            raise ValueError("The colour of the point should be in the list ['red','green','blue','yellow','magenta']")
        new_point = MyPoint(new_coord_x, new_coord_y, new_colour)
        new_point.set_coord_x(new_coord_x)
        new_point.set_coord_y(new_coord_y)
        new_point.set_Colour(new_colour)
        self.points_storage[given_index] = new_point

    def get_points_inside_a_given_square(self, up_left_x, up_left_y, length):
        '''

        :param up_left_x:
        :param up_left_y:
        :param length:
        :return:
        '''
        down_left_x = up_left_x
        down_left_y = up_left_y - length
        up_right_x = up_left_x + length
        up_right_y = up_left_y
        down_right_x = up_right_x
        down_right_y = down_left_y
        '''
        print(down_left_x)
        print(down_left_y)
        print(up_right_x)
        print(up_right_y)
        print(down_right_x)
        print(down_right_y)
        '''
        list_of_points = self.get_all_points()
        for point in list_of_points:
            if point.coord_x > down_left_x and point.coord_x < down_right_x and point.coord_y > down_left_y and point.coord_y < up_left_y:
                print(point)

    def get_the_minimum_distance_between_two_point(self):
        '''

        :return:
        '''
        minimum_distance = 999999999999999
        list_of_points = self.get_all_points()
        for i in range(len(list_of_points) - 1):
            for j in range(i + 1, len(list_of_points)):
                if (list_of_points[i].coord_x - list_of_points[j].coord_x) ** 2 + (list_of_points[i].coord_y -
                                                                                   list_of_points[
                                                                                       j].coord_y) ** 2 < minimum_distance:
                    minimum_distance = (list_of_points[i].coord_x - list_of_points[j].coord_x) ** 2 + (
                            list_of_points[i].coord_y -
                            list_of_points[j].coord_y) ** 2
        return minimum_distance ** 0.5

    def delete_a_point_by_index(self, given_index):
        '''

        :param given_index:
        :return:
        '''
        if given_index < 0 or given_index >= len(self.points_storage):
            raise IndexError("The index is out of range!")
        del self.points_storage[given_index]

    def get_all_points(self):
        '''

        :return:
        '''
        return deepcopy(self.points_storage)
