from Domain.Infrastructure.Utils import append_in_the_list, insertion , delete_index, delete_index_index ,prime_numbers_in_list,odd_numbers_list,replace_array_with_subarray,prime,odd_number,sum_of_numbers, gcd_of_two_numbers , gcd_in_a_list,maximum_in_a_list , negative_number , filter_prime_numbers ,filter_negative_numbers
def test_append_in_the_list():

    assert append_in_the_list([1,2,3],5)==[1,2,3,5]
    assert append_in_the_list([10,1,20],25)==[10,1,20,25]
    assert append_in_the_list([10,20,30],0)==[10,20,30,0]
    assert append_in_the_list([7,12,15],3000)==[7,12,15,3000]
    assert append_in_the_list([13,15,17,19],23)==[13,15,17,19,23]

def test_insertion():

    assert insertion([4,5,6,10],2,5)==[4,5,5,6,10]
    assert insertion([3,9,10,4,5],3,3)==[3,9,10,3,5]
    assert insertion([7,51,1],0,1000)==[1000,7,51,1]
    assert insertion([10,20,30],0,0)==[0,10,20,30]
    assert insertion([20,30,40],3,50)==[20,30,40,50]

def test_delete_index():

    assert delete_index([3,4,5,10,12,15],2)==[3,4,10,12,15]
    assert delete_index([1,2,3,4],0)==[2,3,4]
    assert delete_index([1,3,4,7,8,12,14,15],2)==[1,3,7,8,12,14,15]
    assert delete_index([7,4,2,31,3,1,10],3)==[7,4,2,3,1,10]
    assert delete_index([14,10,5,11,10,7,6],2)==[14,10,11,10,7,6]

def test_prime_numbers_in_list():
    assert prime_numbers_in_list([2,3,7,11,19,20,30,40],0,2)==[2,3,7]
    assert prime_numbers_in_list([10,10,10,10],0,3)==[]
    assert prime_numbers_in_list([11,10,9,8,7,11],1,4)==[7]
    assert prime_numbers_in_list([14,35,37,233,11],2,4)==[37,233,11]
    assert prime_numbers_in_list([2,4,6,8,10,12,14,16,13,14,15,16,17],0,5)==[]


def test_delete_index_index():

    assert delete_index_index([1,2,3,4,5,6,7],1,4)==[1,6,7]
    assert delete_index_index([10,9,8,7,6,5],2,4)==[10,9,5]
    assert delete_index_index([7,5,3,1,0],1,3)==[7,0]
    assert delete_index_index([4,5,6,7,8,9,10],2,4)==[4,5,9,10]
    assert delete_index_index([10,20,30,40,50,60],1,3)==[10,50,60]

def test_replace_array_with_subarray():

    assert replace_array_with_subarray([1,2,3,4,5,7,8],[1,2],[100])==[100,3,4,5,7,8]
    assert replace_array_with_subarray([2,4,6,2,4,6],[2,4,6],[300])==[300,300]
    assert replace_array_with_subarray([99,10,99,99,100],[99,99],[100])==[99,10,100,100]
    assert replace_array_with_subarray([30,5,20,20,4],[20],[30])==[30,5,30,30,4]
    assert replace_array_with_subarray([15,19,18,17],[19,18],[2000])==[15,2000,17]
def test_prime():

    assert prime(7)==True
    assert prime(11)==True
    assert prime(4)==False
    assert prime(222)==False
    assert prime(45)==False

def test_odd_number():

    assert odd_number(7)==True
    assert odd_number(6)== False
    assert odd_number(98989)==True
    assert odd_number(828) == False
    assert odd_number(725)==True

def test_sum_of_numbers():

    assert sum_of_numbers([1,7,9,10,3,4,5],3,5)== 17
    assert sum_of_numbers([12,10,8,6,4,2,0],0,3) == 36
    assert sum_of_numbers([3,5,7,9,11],0,2) == 15
    assert sum_of_numbers([1,2,3,5,19,20],1,3) == 10
    assert sum_of_numbers([5,5,5,5,5,5,5,5],0,7) == 40
def test_gcd_of_two_numbers():

    assert gcd_of_two_numbers(12,48) == 12
    assert gcd_of_two_numbers(0,600) == 600
    assert gcd_of_two_numbers(601, 600) == 1
    assert gcd_of_two_numbers(20,80) == 20
    assert gcd_of_two_numbers(400,200) == 200

def test_gcd_in_a_list():

    assert gcd_in_a_list([2,4,6,8,10],0,2)==2
    assert gcd_in_a_list([3,6,9,12,15],0,4)==3
    assert gcd_in_a_list([1,2,3,4,5],0,2)==1
    assert gcd_in_a_list([1,2,3,7,11,13,17,19,23,29,31,37],0,6)==1
    assert gcd_in_a_list([1,3,5,7,9,11,1,3,5,7,9],0,3)==1
    assert gcd_in_a_list([10,5,10,20,30,40,50],2,5)==10
def test_maximum_in_a_list():

    assert maximum_in_a_list([900,0,3,4,5,10],0,3)==900
    assert maximum_in_a_list([1200,3000,40,5,10000,304],1,3)==3000
    assert maximum_in_a_list([50,400,10,200,30],0,2)==400
    assert maximum_in_a_list([750,3000,20,3000,20,750,4000],0,6)==4000
    assert maximum_in_a_list([25,766,30,50,0,2000,300000,101913,203,40],1,3)==766


def test_negative_number():
    assert negative_number(25)==False
    assert negative_number(-4)==True
    assert negative_number(775) == False
    assert negative_number(-25) == True
    assert negative_number(5) == False

def test_filter_prime_numbers():
    assert filter_prime_numbers([2,3,11,20,30])==[2,3,11]
    assert filter_prime_numbers([0,2,4,6,8])==[2]
    assert filter_prime_numbers([1,3,5,7,11])==[3,5,7,11]
    assert filter_prime_numbers([4,6,8,10,20,40,51,223])==[223]
    assert filter_prime_numbers([23,-5,10,40,20,19])==[23,19]
def test_filter_negative_numbers():
    assert filter_negative_numbers([-3,-4,-2,-10])==[-3,-4,-2,-10]
    assert filter_negative_numbers([-2,11,-3,14])==[-2,-3]
    assert filter_negative_numbers([1,3,7,19])==[]
    assert filter_negative_numbers([3,7,22,455,22])==[]
    assert filter_negative_numbers([22,-22,22,-22,22,-22])==[-22,-22,-22]
def run_all_tests_and_examples():
    test_append_in_the_list()
    test_delete_index()
    test_delete_index_index()
    test_replace_array_with_subarray()
    test_prime()
    test_odd_number()
    test_sum_of_numbers()
    test_gcd_in_a_list()
    test_maximum_in_a_list()
    test_negative_number()
    test_filter_negative_numbers()
    test_filter_prime_numbers()
    data_examples_iteration1()
    data_examples_iteration2()
    data_examples_iteration3()

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
    delete_index(my_list,1)    #date example number 7 , delete the first element of the list
    print(my_list)
    delete_index_index(my_list,2,4)     #date example number 8 , delete the elements of the list from 2 to 4
    print(my_list)
    delete_index(my_list, 3)  # date example number 9 delete the 3rd element of the list
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


def data_examples_iteration2():

    my_list1=[1,3,5,10,20,200,30,4,1,3,5,1,3,5,10,20,4,40,500,430,25,70,35,50,15,20,15,27,35,223,17,11,29,32,37,20]
    print(odd_numbers_list(my_list1,0,3))        #date example number 1 , print the odd numbers from index 2 to index 6
    print(prime_numbers_in_list(my_list1,0,5))     #date example number 2 , print the prime numbers from index 2 to index 6
    print(sum_of_numbers(my_list1,5,7))          #date example number 3 , print the sum beetween 5 and 7 in list
    print(sum_of_numbers(my_list1,10,12))      #date example number 4 print the sum beetween 10 and 12 in list
    print(gcd_in_a_list(my_list1,3,5))  #date example number 5 , compute gcd in a list in the interval [3,5]
    print(gcd_in_a_list(my_list1, 10, 12)) #date example number 6 , compute gcd in a list in the interval [3,5]
    print(maximum_in_a_list(my_list1,0,3)) #date example number 7 , compute the greatest element in a list in the interval [0,3]
    print(maximum_in_a_list(my_list1, 5, 8)) #date example number 8 , compute the greatest element in a list in the interval [0,3]
    print(maximum_in_a_list(my_list1, 12, 13)) #date example number 9 , compute the greatest element in a list in the interval [12,13]
    print(maximum_in_a_list(my_list1,13,15))         #date example number 10 , compute the greatest element in a list in the interval [13,15]


def data_examples_iteration3():
    my_list1=[7,3,0,-1,0,-7,11,20,9,0,-7]
    my_list2=[-1,3,-5,2,6,22,23,11]
    my_list3=[2,3,6,9,8,-30,-1,-10]
    my_list4=[-2,5,7,-1,37,-99,7,11,-5,-7,13]
    my_list5=[3,7,-1,-7,14,21,-5,-9]
    my_list6=[3,-7,2,10,15,17]
    my_list7=[10,20,30,40,-50]
    my_list8=[11,5,10,20,17,23]
    my_list9=[-1,-3,-5,-7,9,11]
    my_list10=[27,30,33,37,41,223]
    filter_negative_numbers(my_list1)  #date example 1
    print(my_list1)
    filter_negative_numbers(my_list2)   #date example 2
    print(my_list2)
    filter_negative_numbers(my_list3)   #date example 3
    print(my_list3)
    filter_negative_numbers(my_list4)  #date example 4
    print(my_list4)
    filter_negative_numbers(my_list5) #date example 5
    print(my_list5)
    filter_prime_numbers(my_list6)       #date example 6

    print(my_list6)
    filter_negative_numbers(my_list7)   #date example 7
    print(my_list7)
    filter_prime_numbers(my_list8)  #date example 8
    print(my_list8)
    filter_negative_numbers(my_list9) #date example 9
    print(my_list9)
    filter_prime_numbers(my_list10) #date example 10
    print(my_list10)