'''
@author: Panaite Cosmin
Modular progamming used for 3 iterations
'''
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
    print("12.Exit")

def reading_of_list():
    '''
    reading of a list
    :return:
    '''
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
    subarray1=[]
    element1=input()
    while element1!="":
        subarray1.append(int(element1))
        element1=input()
    return subarray1

def reading_of_subarray2():
    '''
    reading of the subarray which will replace the ap
    :return:
    '''
    subarray2=[]
    element2=input()
    while element2!="":
        subarray2.append(int(element2))
        element2=input()
    return subarray2

def reading_of_value():

    value=int(input("value="))
    return value #used to be

def reading_of_value2():

    value2=int(input("value2="))
    return value2 # a value which

def reading_of_index():

    index=int(input("index="))
    return index    #index used to be introduced on a position

def reading_of_m():

    m=int(input("m="))
    return m

def reading_of_n():

    n=int(input("n="))
    return n    # we delete from [m,n]

def reading_of_index2():

    index2=int(input("index2="))
    return index2 #index2 a specific index where i remove a number from list which is on the index3

def reading_of_n1():

    n1=int(input("n1="))
    return n1

def reading_of_n2():

    n2=int(input("n2="))
    return n2  # I use n1, n2 as an interval for function with prime numbers

def reading_of_y1():

    y1=int(input("y1="))
    return y1

def reading_of_y2():

    y2=int(input("y2="))
    return y2  #    I use y1, y2 as an interval for function with odd numbers from y1 to y2


def reading_of_z1():

    z1=int(input("z1="))
    return z1

def reading_of_z2():

    z2=int(input("z2="))
    return z2  #I use z1 and z2 as indices for sum in a list

def reading_of_w1():

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

def append_in_the_list(list1,value):
    '''
    Description:Append a new element in list
    Data:list1,value
    :param list1: the given list
    :param value: an appended value
    :return: result will be an extended list where the last element will be 'value'
    '''
    list1.append(value)
    return list1
    print("\n")

def test_append_in_the_list():

    assert append_in_the_list([1,2,3],5)==[1,2,3,5]
    assert append_in_the_list([10,1,20],25)==[10,1,20,25]
    assert append_in_the_list([10,20,30],0)==[10,20,30,0]
    assert append_in_the_list([7,12,15],3000)==[7,12,15,3000]
    assert append_in_the_list([13,15,17,19],23)==[13,15,17,19,23]

def insertion(list1,index,value2):
    '''
    Description:we insert a new value but in a specified index
    :param list1: the list of elements
    :param index: the index where we add a new value
    :param value: the added value
    :return: the modified list
    '''
    list1.insert(index,value2)
    return list1
    print("\n")

def test_insertion():

    assert insertion([4,5,6,10],2,5)==[4,5,5,6,10]
    assert insertion([3,9,10,4,5],3,3)==[3,9,10,3,5]
    assert insertion([7,51,1],0,1000)==[1000,7,51,1]
    assert insertion([10,20,30],0,0)==[0,10,20,30]
    assert insertion([20,30,40],3,50)==[20,30,40,50]

def delete_index(list1,index2):
    '''
    Description:we delete an element from a specified index
    Data:list1,index2
    :param list1: the given list
    :param index2: the index where we add an element
    :return: The modified subarray with a deleted element which was on index2
    '''
    del (list1[index2])
    return list1
    print("\n")

def test_delete_index():

    assert delete_index([3,4,5,10,12,15],2)==[3,4,10,12,15]
    assert delete_index([1,2,3,4],0)==[2,3,4]
    assert delete_index([1,3,4,7,8,12,14,15],2)==[1,3,7,8,12,14,15]
    assert delete_index([7,4,2,31,3,1,10],3)==[7,4,2,3,1,10]
    assert delete_index([14,10,5,11,10,7,6],2)==[14,10,11,10,7,6]

def delete_index_index(list1,m,n):
    '''
    we delete the elementrs in a list from m to n
    :param list1: the given list
    :param m: the first number of the interval [m,n]
    :param n: the second number of the interval [m,n]
    :return: The modified list where will disappear the elements from m to n
    '''
    del (list1[m:n+1])
    return list1
    print("\n")

def test_delete_index_index():

    assert delete_index_index([1,2,3,4,5,6,7],1,4)==[1,6,7]
    assert delete_index_index([10,9,8,7,6,5],2,4)==[10,9,5]
    assert delete_index_index([7,5,3,1,0],1,3)==[7,0]
    assert delete_index_index([4,5,6,7,8,9,10],2,4)==[4,5,9,10]
    assert delete_index_index([10,20,30,40,50,60],1,3)==[10,50,60]

def replace_array_with_subarray(list_1,list_2,list_3):
    '''
    Description:print the new array where where every appearence of first subarray will  be changed with the second subarray
    :param list_1:the given list
    :param list_2: the first subarray which should be changed with the second
    :param list_3: the second subarray
    :return: the result will be the modified list where every appearence of first subarray will  be changed with the second subarray
    '''
    for i in range(len(list_1)+len(list_3)): #we add +len(list_3) here for the case when we have the array ,which we should change with another one bigger , the last in the list
        if list_1[i:i+len(list_2)] == list_2 :
            list_1[i:i+len(list_2)] = list_3
    return list_1

def test_replace_array_with_subarray():

    assert replace_array_with_subarray([1,2,3,4,5,7,8],[1,2],[100])==[100,3,4,5,7,8]
    assert replace_array_with_subarray([2,4,6,2,4,6],[2,4,6],[300])==[300,300]
    assert replace_array_with_subarray([99,10,99,99,100],[99,99],[100])==[99,10,100,100]
    assert replace_array_with_subarray([30,5,20,20,4],[20],[30])==[30,5,30,30,4]
    assert replace_array_with_subarray([15,19,18,17],[19,18],[2000])==[15,2000,17]

def prime(x):
    '''
    Description:We chech if a number is prime
    Data:x
    Precondition:x-natural number
    Result:The result will be true if the number is prime or prime if it is not prime
    :param x:a number which we verify if is prime or not
    :return: The result will be true if the number is prime or prime if it is not prime
    '''
    if x<2:
        return False
    for d in range (2,int(x**(0.5))+1):
        if x%d==0:
            return False
    return True

def test_prime():

    assert prime(7)==True
    assert prime(11)==True
    assert prime(4)==False
    assert prime(222)==False
    assert prime(45)==False

def prime_numbers_in_list(list1,n1,n2):
    '''
    Descriptiom:we print the prime numbers from n1 to n2 in a list
    Data:list1,n1,n2
    Precondition:n1,n2-natural numbers
    Result:The result will be the elements of the list which are prime
    :param list1: the given list
    :param n1: first number in the interval
    :param n2: last number in the interval
    :return:The result will be the elements of the list which are prime
    '''
    for i in range (n1,n2+1): #from n1 to n2
        if prime(list1[i])==True:
            print(list1[i], end=" ")
    print("\n")

def odd_number(y):
    '''
    Description:the program returns true if a numbers is odd and false if it is even
    Data:y
    Precondition:y-natural number
    Result: True if the number is odd , false if it is even.
    :param y: the given number
    :return:True if the number is odd , false if it is even.
    '''
    if y%2==0:
        return False
    return True

def test_odd_number():

    assert odd_number(7)==True
    assert odd_number(6)== False
    assert odd_number(98989)==True
    assert odd_number(828) == False
    assert odd_number(725)==True

def odd_numbers_list(list1,y1,y2):
    '''
    Description:We print the odd numbers from y1 to y2
    Data: list1,y1,y2
    Precondition:y1,y2 -natural numbers
    Result: Odd numbers from y1 to y2 in a list
    :param list1: given list
    :param y1: the first number in the interval from the list
    :param y2: the last number in the interval from the list
    :return:Odd numbers from [y1,y2] in a list
    '''
    for i in range(y1,y2+1): #from y1 to y2
        if odd_number(list1[i])==True:
            print(list1[i], end=" ")
    print("\n")


def sum_of_numbers(list1,z1,z2):
    '''
    Description:we compute the from z1 to z2 in a list
    Data: list1,z1,z2
    Precondition:z1 and z2-natural numbers
    Result: The sum of the numbers from[z1,z2] in a list
    :param list1: the given list
    :param z1: the first number in the interval
    :param z2: the last number in the interval
    :return: the sum of the numbers from [z1,z2]
    '''
    sum=0
    for i in range(z1,z2+1): #from z1 to z2
        sum=sum+list1[i]
    return sum  #reult of the sum of numbers from z1 to z2

def test_sum_of_numbers():

    assert sum_of_numbers([1,7,9,10,3,4,5],3,5)== 17
    assert sum_of_numbers([12,10,8,6,4,2,0],0,3) == 36
    assert sum_of_numbers([3,5,7,9,11],0,2) == 15
    assert sum_of_numbers([1,2,3,5,19,20],1,3) == 10
    assert sum_of_numbers([5,5,5,5,5,5,5,5],0,7) == 40

def gcd_of_two_numbers(aux,bux):
    '''
    Description: we compute the greatest common divisor of two numbers
    Data:aux,bux
    Precondition: aux , bux -natural numbers and one of them should be greater than 0
    Result: Will be the gcd of the 2 numbers
    :param aux:
    :param bux:
    :return:
    '''
    if aux==0:
        return bux
    if bux==0:
        return aux
    if aux==0 and bux==0:
        return -1
    while aux!=bux :
        if aux > bux:
            aux = aux-bux
        else:
            bux = bux-aux
    return aux

def test_gcd_of_two_numbers():

    assert gcd_of_two_numbers(12,48) == 12
    assert gcd_of_two_numbers(0,600) == 600
    assert gcd_of_two_numbers(601, 600) == 1
    assert gcd_of_two_numbers(20,80) == 20
    assert gcd_of_two_numbers(400,200) == 200

def gcd_in_a_list(list1,w1,w2):
    '''
    Descr:We compute the gcd in a list from w1 to w2
    Data: list1 w1,w2
    Precondition: w1,w2-natural numbers
    :param list1:
    :param w1:
    :param w2:
    :return: the gcd of the numbers from interval [w1,w2] of the list
    '''
    first_gcd=list1[w1]
    for i in range(w1+1,w2+1):
        second_gcd= gcd_of_two_numbers(first_gcd,list1[i])
        first_gcd=second_gcd
    return first_gcd

def test_gcd_in_a_list():

    assert gcd_in_a_list([2,4,6,8,10],0,2)==2
    assert gcd_in_a_list([3,6,9,12,15],0,4)==3
    assert gcd_in_a_list([1,2,3,4,5],0,2)==1
    assert gcd_in_a_list([1,2,3,7,11,13,17,19,23,29,31,37],0,6)==1
    assert gcd_in_a_list([1,3,5,7,9,11,1,3,5,7,9],0,3)==1
    assert gcd_in_a_list([10,5,10,20,30,40,50],2,5)==10

def maximum_in_a_list(list1,t1,t2):
    '''
    we compute the greatest element  in a list which is in [t1,t2]
    :param list1: the list of elements
    :param t1: the first index of the interval
    :param t2: the second index of the interval
    :return: the greatest element from [t1,t2] in a list
    '''
    maxi=list1[t1]
    for i in range(t1+1,t2+1):
        if(list1[i]>maxi):
            maxi=list1[i]
    return maxi

def test_maximum_in_a_list():

    assert maximum_in_a_list([900,0,3,4,5,10],0,3)==900
    assert maximum_in_a_list([1200,3000,40,5,10000,304],1,3)==3000
    assert maximum_in_a_list([50,400,10,200,30],0,2)==400
    assert maximum_in_a_list([750,3000,20,3000,20,750,4000],0,6)==4000
    assert maximum_in_a_list([25,766,30,50,0,2000,300000,101913,203,40],1,3)==766

def data_examples_iteration1():
    '''
    a set of examples of functions which i used during the project
    :return:
    '''
    my_list = [2, 2, 3, 7, 11, 19, 33, 5, 20, 11, 40, 20, 80, 30, 45, 7, 7, 7, 37, 28, 35, 45, 100, 30, 40, 50, 60, 80]
    my_subarray1 = [7, 7, 7]
    my_subarray2 = [20, 80, 30]
    my_subarray3 = [101, 99, 100]

    append_in_the_list(my_list,30) #date example 1 number append in the list number 30
    print(my_list)
    append_in_the_list(my_list,3030) #date example 2 number append in the list number 300
    print(my_list)
    append_in_the_list(my_list,30) #date example 3 number append in the list number 30
    print(my_list)
    insertion(my_list,0,3000)   #date example number 4 , insert 3000 as the first element of the list
    print(my_list)
    delete_index(my_list,2)     #date example number 5 , delete the 3rd element of the list
    print(my_list)
    delete_index(my_list,7)     #date example number 6 , delete the 8th element of the list
    print(my_list)
    delete_index(my_list,-1)    #date example number 7 , delete the last element of the list
    print(my_list)
    delete_index_index(my_list,2,4)     #date example number 8 , delete the elements of the list from 2 to 4
    print(my_list)
    delete_index(my_list, -2)  # date example number 9 delete the penultimate(second to last) element of the list
    print(my_list)
    insertion(my_list, 7, 2525) #date example 10 ,2525 will be inserted as 8th element of the list
    print(my_list)
    insertion(my_list,10,90) #date example 11 , 90 will be inserted as 11th element of the list
    print(my_list)
    replace_array_with_subarray(my_list, my_subarray1, my_subarray3)  # date example number 12 , change an subarray with a random subarray
    print(my_list)
    replace_array_with_subarray(my_list, my_subarray2, my_subarray3)  # date example number 13 , change an subarray with a random subarray
    print(my_list)
    replace_array_with_subarray(my_list, [2, 2], [1, 1])  # date example number , 14 change an subarray with a random subarray
    print(my_list)
data_examples_iteration1()

def data_examples_iteration2():

    my_list1=[1,3,5,10,20,200,30,4,1,3,5,1,3,5,10,20,4,40,500,430,25,70,35,50,15,20,15,27,35,223,17,11,29,32,37,20]
    odd_numbers_list(my_list1,2,6)        #date example number 1 , print the odd numbers from index 2 to index 6
    prime_numbers_in_list(my_list1,2,26)      #date example number 2 , print the prime numbers from index 2 to index 6
    print(sum_of_numbers(my_list1,5,7))          #date example number 3 , print the sum beetween 5 and 7 in list
    print(sum_of_numbers(my_list1,10,12))      #date example number 4 print the sum beetween 10 and 12 in list
    print(gcd_in_a_list(my_list1,3,5))  #date example number 5 , compute gcd in a list in the interval [3,5]
    print(gcd_in_a_list(my_list1, 10, 12)) #date example number 6 , compute gcd in a list in the interval [3,5]
    print(maximum_in_a_list(my_list1,0,3)) #date example number 7 , compute the greatest element in a list in the interval [0,3]
    print(maximum_in_a_list(my_list1, 5, 8)) #date example number 8 , compute the greatest element in a list in the interval [0,3]
    print(maximum_in_a_list(my_list1, 12, 13)) #date example number 9 , compute the greatest element in a list in the interval [12,13]
    print(maximum_in_a_list(my_list1,13,15))         #date example number 10 , compute the greatest element in a list in the interval [13,15]

data_examples_iteration2()



def main():
    '''
    options
    '''
    list1=[]

    while True:
        print_menu()
        option=int(input("Introduce the number of option:"))
        if option == 1:
            list1=reading_of_list()
        elif option == 2:
            value = reading_of_value()
            print(append_in_the_list(list1,value))

        elif option == 3:
            index = reading_of_index()
            value2 = reading_of_value2()
            print(insertion(list1,index,value2))

        elif option == 4:
            index2=reading_of_index2()
            print(delete_index(list1,index2))

        elif option == 5:
            m = reading_of_m()
            n = reading_of_n()
            print(delete_index_index(list1,m,n))

        elif option == 6:
            subarray1 = reading_of_subarray()
            subarray2 = reading_of_subarray2()
            print(replace_array_with_subarray(list1,subarray1,subarray2))
        elif option == 7:
            n1=reading_of_n1()
            n2=reading_of_n2()
            prime_numbers_in_list(list1,n1,n2)
        elif option == 8:
            y1=reading_of_y1()
            y2=reading_of_y2()
            odd_numbers_list(list1,y1,y2)
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
            break

        else:
            print("Option is invalid")

test_append_in_the_list()
test_delete_index()
test_delete_index_index()
test_replace_array_with_subarray()
test_prime()
test_odd_number()
test_sum_of_numbers()
test_gcd_in_a_list()
test_maximum_in_a_list()
main()



