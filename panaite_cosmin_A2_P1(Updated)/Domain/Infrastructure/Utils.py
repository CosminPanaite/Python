import copy

def prime(x):
    '''
    I check if a number is prime or not
    Data:x
    Precondition:x-natural number
    :param x: given number
    :return: the result will be a false if number is not prime and true if it is
    '''
    if x < 2:
        return False

    for i in range(2, int(x ** (0.5) + 1)):
        if x % i == 0:
            return False
    return True

def append_in_the_list(list1,value):
    '''
    Description:Append a new element in list
    Data:list1,value
    :param list1: the given list
    :param value: an appended value
    :return: result will be an extended list where the last element will be 'value'
    '''
    if len(list1)==0:
        print("My list is empty")
        return False
    list1.append(value)
    return list1


def insertion(list1,index,value2):
    '''
    Description:we insert a new value but in a specified index
    :param list1: the list of elements
    :param index: the index where we add a new value
    :param value: the added value
    :return: the modified list
    '''
    if len(list1)==0:
        print("The list is empty")
        return False
    if index>len(list1):
        print("The index is out of range ")
        return False
    if index<0:
        print("The negative index is meaningless for user")
        return False

    list1.insert(index,value2)
    return list1


def delete_index(list1,index2):
    '''
    Description:we delete an element from a specified index
    Data:list1,index2
    :param list1: the given list
    :param index2: the index where we add an element
    :return: The modified subarray with a deleted element which was on index2
    '''
    if len(list1)==0:
        print("The list is empty")
        return False
    if index2>=len(list1):
        print("The index is out of range ")
        return False
    if index2<0:
        print("The negative index2 is meaningless for user")
        return False

    del (list1[index2])
    return list1



def delete_index_index(list1,m,n):
    '''
    we delete the elementrs in a list from m to n
    :param list1: the given list
    :param m: the first number of the interval [m,n]
    :param n: the second number of the interval [m,n]
    :return: The modified list where will disappear the elements from m to n
    '''
    if len(list1) == 0:
        print("The list is empty")
        return False
    if m > n:
        print("It's an error ,because we work in range , increasing , so we exclude the cases where m>n")
        return False
    if n < 0:
        print("Negative values of m and n are meaningless for the user")  # it implies that m<n<0
        return False
    if m < 0:
        print("Negative values of n1 are meaningless for the user")
        return False
    if m > len(list1):
        print("Both indices are out of range")  # i don t make another if with m and n > len , because it implies  both of indices , because I said that m>n is false
        return False
    if n > len(list1):
        print("n2 is out of range")
        return False
    del (list1[m:n+1])
    return list1

def replace_array_with_subarray(list_1,list_2,list_3):
    '''
    Description:print the new array where where every appearence of first subarray will  be changed with the second subarray
    :param list_1:the given list
    :param list_2: the first subarray which should be changed with the second
    :param list_3: the second subarray
    :return: the result will be the modified list where every appearence of first subarray will  be changed with the second subarray
    '''


    if len(list_1)==0:
        print("The list is empty , we can't change something")
        return False
    if len(list_2)==0:
        print("The subarray is empty , we can't change something")
        return False
    for i in range(len(list_1)+len(list_3)): #we add +len(list_3) here for the case when we have the array ,which we should change with another one bigger , the last in the list
        if list_1[i:i+len(list_2)] == list_2 :
            list_1[i:i+len(list_2)] = list_3
    return list_1
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
    new_list1=[]
    if len(list1)==0:
        print("The list is empty")
        return False
    if n1>n2:
        print("It's an error ,because we work in range , increasing , so we exclude the cases where n1>n2")
        return False
    if n2 < 0:
        print("Negative values of n1 and n2 are meaningless for the user") #it implies that n1<n2<0
        return False
    if n1 < 0:
        print("Negative values of n1 are meaningless for the user")
        return False
    if n1>=len(list1):
        print("Both indices are out of range") # i don t make another if with n1 and n2 > len , because it implies  both of indices , because I said that n1>n2 is false
        return False
    if n2 > len(list1):
        print("n2 is out of range")
        return False
    for i in range (n1,n2+1): #from n1 to n2
        if prime(list1[i])==True:
            new_list1.append(list1[i])
    return new_list1

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
    new_list=[]
    if len(list1)==0:
        print("The list is empty")
        return False
    if y1>y2:
        print("It's an error ,because we work in range , increasing , so we exclude the cases where y1>y2")
        return False
    if y2 < 0:
        print("Negative values of y1 and y2 are meaningless for the user") #it implies that y1<y2<0
        return False
    if y1 < 0:
        print("Negative values of y1 are meaningless for the user")
        return False
    if y1>=len(list1):
        print("Both indices are out of range") # i don t make another if with y1 and y2 > len , because it implies  both of indices , because I said that y1>y2 is false
        return False
    if y2 > len(list1):
        print("y2 is out of range")
        return False
    for i in range(y1,y2+1): #from y1 to y2
        if odd_number(list1[i])==True:
            new_list.append(list1[i])
    return new_list


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
    if len(list1)==0:
        print("I'll give to sum value -1")
        return -1 # a special value for sum if the list is empty
    if z1 > z2:
        print("It's an error ,because we work in range , increasing , so we exclude the cases where z1>z2")
        return False
    if z2 < 0:
        print("Negative values of z1 and z2 are meaningless for the user")  # it implies that z1<z2<0
        return False
    if z1 < 0:
        print("Negative values of z1 are meaningless for the user")
        return False
    if z1 >= len(list1):
        print("Both indices are out of range")  # i don t make another if with z1 and z2 > len , because it implies  both of indices , because I said that z1>z2 is false
        return False
    if z2 > len(list1):
        print("z2 is out of range")
        return False

    sum=0
    for i in range(z1,z2+1): #from z1 to z2
        sum=sum+list1[i]
    return sum  #reult of the sum of numbers from z1 to z2

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
    while aux!=bux :
        if aux > bux:
            aux = aux-bux
        else:
            bux = bux-aux
    return aux

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
    if len(list1)==0:
        print("My list is empty and i give the gcd value -1")
        return -1 # i prefer -1 to be the value if the list is empty
    if w1 > w2:
        print("It's an error ,because we work in range , increasing , so we exclude the cases where w1>w2")
        return False
    if w2 < 0:
        print("Negative values of w1 and w2 are meaningles for the user")  # it implies that w1<w2<0
        return False
    if w1 < 0:
        print("Negative values of w1 are meaningless for the user")
        return False
    if w1 >= len(list1):
        print("Both indices are out of range")  # i don t make another if with w1 and w2 > len , because it implies  both of indices , because I said that w1>w2 is false
        return False
    if w2 > len(list1):
        print("w2 is out of range")
        return False

    for i in range(len(list1)-1):
        if list1[i]==0 and list1[i+1]==0:
            return -1
    first_gcd=list1[w1]
    for i in range(w1+1,w2+1):
        second_gcd= gcd_of_two_numbers(first_gcd,list1[i])
        first_gcd=second_gcd
    return first_gcd

def maximum_in_a_list(list1,t1,t2):
    '''
    we compute the greatest element  in a list which is in [t1,t2]
    :param list1: the list of elements
    :param t1: the first index of the interval
    :param t2: the second index of the interval
    :return: the greatest element from [t1,t2] in a list
    '''
    if len(list1)==0:
        print("The list is empty")
        return -1 #i prefer -1 to be the the value if the we have empty list
    if t1>t2:
        print("It's an error ,because we work in range , increasing , so we exclude the cases where w1>w2")
        return False
    if t2 < 0:
        print("Negative values of t1 and t2 are meaningles for the user") #it implies that t1<t2<0
        return False
    if t1 < 0:
        print("Negative values of t1 are meaningless for the user")
        return False
    if t1 >= len(list1):
        print("Both indices are out of range") # i don t make another if with t1 and t2 > len , because it implies  both of indices , because I said that t1>t2 is false
        return False
    if t2 > len(list1):
        print("t2 is out of range")
        return False
    maxi=list1[t1]
    for i in range(t1+1,t2+1):
        if(list1[i]>maxi):
            maxi=list1[i]
    return maxi



def negative_number(y):
    '''
    I check if a number is negative or not
    Data- y
    :param y: a given number
    :return: the result will be true if the number is negative and false if not
    '''

    if y < 0:
        return True
    return False

def filter_prime_numbers(list1):
    '''
    I keep in the list only the prime numbers.
    Data:list1
    :param list1: given list
    :return: The result will be the new array
    '''

    i = 0
    leng=len(list1)

    while i <=leng-1 :
        if prime(list1[i]) == False:
            list1.pop(i)
            leng=leng-1
        else:
            i=i+1

    return list1
def filter_negative_numbers(list1):
    '''
    I keep in the list only negative numbers.
    Data:list1
    :param list1: a given list
    :return: The result will be the new array
    '''
    i=0
    leng=len(list1)
    while i<=leng-1:
        if negative_number(list1[i])==False:
            list1.pop(i)
            leng=leng-1
        else:
            i =i+1

    return list1
def add_history(list1,history):
    '''
    Description:in history we append the last copy of list1 for creating a history
    :param list1: the given list
    :param history:with help of deepcopy i create in history a list of lists
    :return: the list of lists
    '''
    history.append(copy.deepcopy(list1)) #i use a deep copy for a list of lists named history


def undo(list1,history):
    '''
    Description:a function which undoes an operation
    :param list1: the given list
    :param history:the list of lists
    :return: return the previous list
    '''
    if len(history)==0:
        print("We can't make an undo operation")
        return False
    else:
        list1=copy.deepcopy(history[-1]) #last list from history
        history.pop()
        return list1