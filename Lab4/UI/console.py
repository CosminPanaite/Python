from Controller.ctrl import VectorController
from Domain.MyVector import MyVector


class Console:
    def __init__(self, list_of_vectors: VectorController):
        self.__list_of_vectors = list_of_vectors

    def print_menu(self):
        print("1.  Add a vector to the repository")
        print("2.  Get all vectors")
        print("3.  Get a vector at a given index")
        print("4.  Update a vector at a given index")
        print("5.  Update a vector identified by name_id")
        print("6.  Delete a vector by index")
        print("7.  Delete a vector by name_id")
        print("8.  Plot all vectors in a chart based on the type and colour of each vector")
        print("9.  Get the vector which represents the sum of all vectors")
        print("10. Get the list of vectors having the minimum less than a given value.")
        print("11. Identify departments where there are patients under a given age")
        print("12. Identify patients from a given department for which the first name or last name contain a given string")
        print("13. Identify department/departments where there are patients with a given first name")

    def run_console(self):
        while True:
            self.print_menu()
            option = int(input("Introduce the option: "))
            if option == 1:
                self.UI_add_a_vector()
            elif option == 2:
                self.UI_get_all_vectors()
                print()
            elif option == 3:
                self.UI_get_a_vector_at_index()
            elif option == 4:
                self.UI_update_a_vector()
            elif option == 5:
                self.UI_update_a_vector_by_name()
            elif option == 6:
                self.UI_delete_a_vector_by_index()
            elif option == 7:
                self.UI_delete_a_vector_by_name()
            elif option == 8:
                self.UI_plot_vectors()
            elif option == 9:
                self.UI_get_the_sum_of_all_vectors()
            elif option == 10:
                self.UI_get_the_list_of_vector_with_minimum_elements()
            elif option == 11:
                break
            else:
                print("Option is invalid ! The end!")

    def UI_add_a_vector(self):
        try:
            name_id = input("name_id= ")
            colour = input("colour= ")
            vector_type = int(input("vector_type= "))
            values = []
            element = input("Introduce a value for the list: ")
            while element != "":
                values.append(int(element))
                element = input("Introduce a value for the list: ")
            self.__list_of_vectors.ctrl_add_a_vector(name_id, colour, vector_type, values)
        except ValueError as ve:
            print("Retry!", ve)
        except Exception as e:
            print("Error", e)

    def UI_get_all_vectors(self):
        vectors_storage = self.__list_of_vectors.ctrl_get_all_vectors()
        for vec in vectors_storage:
            print(vec , end=" ; ")
    def UI_get_a_vector_at_index(self):
        try:
            index=int(input("Index="))
            print(self.__list_of_vectors.ctrl_get_a_vector_at_an_index(index))
        except ValueError as ve:
            print("Introduce correct data",ve)
        except IndexError:
            print("Introduce correct index")
        except Exception as e:
            print("Solve error!" , e)
    def UI_update_a_vector(self):
        try:
            index=int (input("index= "))
            new_colour = input("colour= ")
            new_vector_type = int(input("vector_type= "))
            new_values = []
            element = input("Introduce a value for the list: ")
            while element != "":
                new_values.append(int(element))
                element = input("Introduce a value for the list: ")
            self.__list_of_vectors.ctrl_update_a_vector(index, new_colour, new_vector_type, new_values)
        except ValueError as ve :
            print("Introduce valid data",ve)
        except IndexError as ie :
            print('Give a valid index!',ie)
    def UI_update_a_vector_by_name(self):
        try:
            name_id= input("name_id= ")
            new_colour = input("colour= ")
            new_vector_type = int(input("vector_type= "))
            new_values = []
            element = input("Introduce a value for the list: ")
            while element != "":
                new_values.append(int(element))
                element = input("Introduce a value for the list: ")

            self.__list_of_vectors.ctrl_update_a_vector_by_name(name_id, new_colour, new_vector_type,new_values)
        except ValueError as ve:
            print("Introduce correct values!",ve)
        except Exception as e:
            print("Solve error!" , e)
    def UI_delete_a_vector_by_index(self):
        try:
            index = int(input("index= "))
            self.__list_of_vectors.ctrl_delete_a_vector_by_index(index)
        except ValueError as ve:
            print("Reintroduce a correct value!", ve)
        except IndexError as ie :
            print("Introduce correct index!" ,ie)
    def UI_delete_a_vector_by_name(self):
        try:
            name_id=input("name_id= ")
            self.__list_of_vectors.ctrl_delete_a_vector_by_name(name_id)
        except ValueError as ve:
            print("Reintroduce correct data!" , ve)


    def UI_get_the_sum_of_all_vectors(self):
        try:
            print(self.__list_of_vectors.ctrl_get_the_sum_of_all_vectors())
        except ValueError as ve:
            print("Introduce correct data!" , ve)
    def UI_get_the_list_of_vector_with_minimum_elements(self):
        try:
            given_min=int(input("given_min= "))
            vectors_storage = self.__list_of_vectors.ctrl_get_the_list_of_vector_with_minimum_elements(given_min)
            for vec in vectors_storage:
                print(vec, end=" ; ")
            print()

        except ValueError as ve:
            print("Introduce correct data!", ve)
    def UI_plot_vectors(self):
        try:
            self.__list_of_vectors.ctrl_plot_vectors()
        except ValueError as ve:
            print("Introduce correct data",ve)