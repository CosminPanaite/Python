# The sum of even numbers
def sum(n):
    '''
    sum of even numbers
    :param n:
    :return:
    '''
    i=0
    s=0
    while i<n: # until i < 7
        s=s+i
        i=i+2 # i will add only even numbers
    return (s)
n=int(input("n="))
print("The sum of even numbers up to 7 is",sum(n))
# Prime number

def primeee(n):
    '''
    prime number algorithm , input -> integer n
    :return:
    '''

    if n<2: # if the number is 0 or 1 it is not prime
        return False
    for d in range (2,int(n**0.5+1)): # i went until square root of n +1
        if n%d==0: #if the number is divisible with d it is not prime
            print("The number is not prime")
    print("The number is prime")
n=int(input("n="))
primeee(n)
