from Repository.my_point_repository import PointRepository


class Console:

    def __init__(self):
        self.list_of_points = PointRepository()

    def print_menu(self):
        print("1. Add a point to the repository")
        print("2. Get all points")
        print("3. Get a point at a given index")
        print("4. Get all points of a given colour")
        print("5. Get all points that are inside a given square")
        print("6. Get the minimum distance between two points")
        print("7. Update a point at a given index")
        print("8. Delete a point by index")
        print("9. Delete all points that are inside a given square")
        print("10. Plot all points in a chart")

    def run_console(self):
        while True:
            self.print_menu()
            option = int(input("Introduce the option:"))
            if option == 1:
                self.ui_add_point_to_the_repository()
            elif option == 2:
                self.ui_get_all_points()
            elif option == 3:
                self.ui_get_a_point_at_a_given_index()
            elif option == 4:
                self.ui_get_all_points_of_a_given_colour()
            elif option == 5:
                self.ui_get_points_inside_a_given_square()
            elif option == 6:
                self.ui_get_the_minimum_distance_between_two_point()
            elif option == 8:
                self.ui_delete_a_point_by_index()
            elif option == 7:
                self.ui_update_a_point_at_a_given_index()
            elif option == 11:
                break
            else:
                print("Invalid option")

    def ui_add_point_to_the_repository(self):
        try:
            coord_x = float(input("coord_x= "))
            coord_y = float(input("coord_y= "))
            colour = input("colour= ")
            self.list_of_points.add_point_to_the_repository(coord_x, coord_y, colour)
        except ValueError as ve:
            print("Reintroduce valid data!", ve)
        except TypeError as te:
            print("Wrong operations", te)
        except Exception as e:
            print("Error", e)

    def ui_get_all_points(self):
        points = self.list_of_points.get_all_points()
        for point in points:
            print(point)

    def ui_get_a_point_at_a_given_index(self):
        try:
            index = int(input("given_index:"))
            print(self.list_of_points.get_a_point_at_a_given_index(index))
        except ValueError as ve:
            print("Reintoduce an integer number", ve)
        except IndexError as ie:
            print(ie)
        except Exception as e:
            print("Error", e)

    def ui_delete_a_point_by_index(self):
        try:
            index_to_be_deleted = int(input("Give me the index: "))
            self.list_of_points.delete_a_point_by_index(index_to_be_deleted)
        except ValueError as ve:
            print("Reintoduce an integer number", ve)
        except IndexError as ie:
            print('Give a valid index!', ie)
        except Exception as e:
            print("Error!", e)

    def ui_update_a_point_at_a_given_index(self):
        try:
            given_index = int(input("given_index= "))
            coord_x = float(input("cooord_x= "))
            coord_y = float(input("cooord_y= "))
            colour = str(input("colour="))
            self.list_of_points.update_a_point_at_a_given_index(given_index, coord_x, coord_y, colour)
        except ValueError as ve:
            print("Introduce valid data", ve)
        except IndexError as ie:
            print('Give a valid index!', ie)
        except Exception as e:
            print("Error!", e)

    def ui_get_the_minimum_distance_between_two_point(self):
        print(self.list_of_points.get_the_minimum_distance_between_two_point())

    def ui_get_all_points_of_a_given_colour(self):
        try:
            colour = input("colour= ")
            print(self.list_of_points.get_all_points_of_a_given_colour(colour))
        except ValueError as ve:
            print("Introduce a valide colour", ve)
        except Exception as e:
            print("Error! ", e)

    def ui_get_points_inside_a_given_square(self):

        try:
            up_left_x = float(input("up_left_x= "))
            up_left_y = float(input("up_left_y= "))
            length = float(input("length= "))
            self.list_of_points.get_points_inside_a_given_square(up_left_x, up_left_y, length)
        except ValueError as ve:
            print('Introduce float numbers!', ve)
        except Exception as e:
            print("Error! ", e)