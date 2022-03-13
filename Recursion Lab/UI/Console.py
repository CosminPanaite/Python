from Domain.functions import gcd_recursive
from Domain.functions import given_power
def print_menu():
    print("1. The gcd of 2 numbers recursive ")
    print("2. The given power of a given number")
def console():
    while True:
        print_menu()
        option = int(input("Introduce the option: "))
        if option==1:
            try:
                number1=int(input("number1= "))
                number2=int(input("number2= "))
                print(gcd_recursive(number1,number2))
            except ValueError as ve:
                print("Retry! " ,ve )
        elif option==2:
            try:
                default_base=int(input("default_base= "))
                power=int(input("power= "))
                print(given_power(default_base, power))
            except ValueError as ve:
                print("Retry! ", ve)
        elif option ==3:
            print("The end!","Bye,Bye!")
            break

        else:
            print("Option is invalid ! The end!")