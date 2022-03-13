'''
Iteration 1,2,3-Modular programming
@author Panaite Cosmin
'''
from Domain.Infrastructure.Utils import append_in_the_list ,insertion , delete_index ,delete_index_index ,replace_array_with_subarray,prime_numbers_in_list,gcd_in_a_list,maximum_in_a_list ,sum_of_numbers,odd_numbers_list, filter_prime_numbers, filter_negative_numbers,undo,add_history


def print_menu():
    print("1.Reading of dates")
    print("2.Append a value in the list")
    print("3.Insertion at index")
    print("4.Delete an element with a specific index")
    print("5.Delete an interval from a list")
    print("6.Replace an subarray with another subarray")
    print("7.Print the numbers which are prime")
    print("8.Print the odd numbers from the array found at indices ")
    print("9.The sum of numbers found at  indices ")
    print("10.The gcd found at indices")
    print("11.Print the maximum found at indices")
    print("12.Filter prime numbers")
    print("13.Filter negative numbers")
    print("14.Undo-operation")
def reading_of_list():
    list1=[]
    element=input()
    while element!="":
        list1.append(int(element))
        element=input()
    return list1
def reading_of_subarray():
    '''
    reading of a sublist which will appear in the list
    :return:
    '''
    list2=[]
    element1=input()
    while element1!="":
        list2.append(int(element1))
        element1=input()
    return list2

def reading_of_subarray2():
    '''
    reading of the subarray which will replace the ap
    :return:
    '''
    list3=[]
    element2=input()
    while element2!="":
        list3.append(int(element2))
        element2=input()
    return list3

def reading_of_value():
    '''
    reading of value which will be appended in the list
    :return:
    '''
    value=int(input("value="))
    return value

def reading_of_value2():
    '''
    reading of value which will be inserted on an index
    :return:
    '''
    value2=int(input("value2="))
    return value2 # a value which

def reading_of_index():
    '''
    reading of an index where i will introduce value 2 in option 3
    :return:
    '''
    index=int(input("index="))
    return index    #index used to be introduced on a position

def reading_of_index2():
    '''
    reading of an index2 which is the index where i delete an element from array
    :return:
    '''
    index2=int(input("index2="))
    return index2 #index2 a specific index where i remove a number from list which is on the index3


def reading_of_m():
    '''
    reading of m which is the first number of the interval used in option 5 for delete
    :return:
    '''
    m=int(input("m="))
    return m

def reading_of_n():
    '''
    reading of n which is the second number of the interval used in option 5 for delete
    :return:
    '''
    n=int(input("n="))
    return n    # we delete from [m,n]


def reading_of_n1():
    '''
    reading of n1 which is the first number of the interval used in option 7 for print the prime numbers
    :return:
    '''
    n1=int(input("n1="))
    return n1

def reading_of_n2():
    '''
    reading of n2 which is the second number of the interval used in option 7 for print the prime numbers
    :return:
    '''
    n2=int(input("n2="))
    return n2  # I use n1, n2 as an interval for function with prime numbers

def reading_of_y1():
    '''
    reading of y1 which is the first number of the interval used in option 8 for printing the odd numbers from the list from interval
    :return:
    '''
    y1=int(input("y1="))
    return y1

def reading_of_y2():
    '''
    reading of y2 which is the second number of the interval used in option 8 for printing the odd numbers from the list from interval
    :return:
    '''
    y2=int(input("y2="))
    return y2  #    I use y1, y2 as an interval for function with odd numbers from y1 to y2


def reading_of_z1():
    '''
    reading of z1 which is the first number of the interval used in option 9 for printing the odd numbers from the list from interval

    :return:
    '''
    z1=int(input("z1="))
    return z1

def reading_of_z2():
    '''
    reading of z2 which is the second number of the interval used in option 9 for printing the odd numbers from the list from interval

    :return:
    '''
    z2=int(input("z2="))
    return z2  #I use z1 and z2 as indices for sum in a list

def reading_of_w1():
    '''
    reading of z1 which is the first number of the interval used in option 9 for printing the odd numbers from the list from interval

    :return:
    '''
    w1=int(input("w1="))
    return w1

def reading_of_w2():

    w2=int(input("w2="))
    return w2 #I use w1 and w2 as indices for gcd in a list

def reading_of_t1():

    t1=int(input("t1="))
    return t1

def reading_of_t2():

    t2=int(input("t2="))
    return t2  #[t1,t2]-> we should find the maximum in this interval


def console():
    '''
    options
    '''
    list1=[]
    list2=[]
    list3=[]
    history=[]

    while True:
        print_menu()
        option=int(input("Introduce the number of option:"))
        if option == 1:
            list1=reading_of_list()
        elif option == 2:

            value = reading_of_value()
            add_history(list1,history)
            print(append_in_the_list(list1,value))

        elif option == 3:

            index = reading_of_index()
            value2 = reading_of_value2()
            add_history(list1,history)
            print(insertion(list1,index,value2))

        elif option == 4:

            index2=reading_of_index2()
            add_history(list1,history)
            print(delete_index(list1,index2))

        elif option == 5:

            m = reading_of_m()
            n = reading_of_n()
            add_history(list1,history)
            print(delete_index_index(list1,m,n))

        elif option == 6:

            list2= reading_of_subarray()
            list3 = reading_of_subarray2()
            add_history(list1,history)
            print(replace_array_with_subarray(list1,list2,list3))
        elif option == 7:
            n1=reading_of_n1()
            n2=reading_of_n2()
            print(prime_numbers_in_list(list1,n1,n2))
        elif option == 8:
            y1=reading_of_y1()
            y2=reading_of_y2()
            print(odd_numbers_list(list1,y1,y2))
        elif option == 9:
            z1=reading_of_z1()
            z2=reading_of_z2()
            print(sum_of_numbers(list1,z1,z2))
        elif option == 10:
            w1=reading_of_w1()
            w2=reading_of_w2()
            print(gcd_in_a_list(list1,w1,w2))
        elif option == 11:
            t1=reading_of_t1()
            t2=reading_of_t2()
            print(maximum_in_a_list(list1,t1,t2))
        elif option ==12:
            print(filter_prime_numbers(list1))
        elif option ==13:
            print(filter_negative_numbers(list1))
        elif option ==14:
            print(undo(list1,history))
        elif option ==15:
            break
        else:
            print("Option is invalid")
