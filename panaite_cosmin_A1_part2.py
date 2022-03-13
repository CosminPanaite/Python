#problem 1 Homework -> Control digit
def digit(n):



    if n % 9 == 0: #if the number is divisible with 9 the control digit will be nine
        return 9
    else:
        return n % 9 # else the control digit will be n%9
n = int(input("n="))
print(digit(n))


# problem 13 Obtain the number 1234-> 13 (odd positions)
def sub(n):
    '''

    :param n:
    :return:
    '''
    inv=0 #the invers of number
    aux=n # a copy for n
    nrnou=0 # a new number 
    while aux!=0:
        inv=inv*10+aux%10
        aux=aux//10
    while inv!=0:
        nrnou=nrnou*10+inv%10
        inv=inv//100
    return nrnou


n=int(input("n="))
print(sub(n))

# Problem 9
#Print all numbers with maximum 2 digits of form xy with the property that the last digit of (xy)2is y.Example: 52=25 or(10)2=100 or(76)2=5776.
def prog():
    '''

    :param d:
    :return:
    '''
    for d in range(1,100):
        if d%10==(d*d)%10:
            print(d)
prog()
