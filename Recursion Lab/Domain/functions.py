def gcd_recursive(number1, number2):
    '''
    compute the gcd of 2 numbers with the aid of recursion
    :param number1: first given number
    :param number2: second given number
    :return:
    '''
    if type(number1) is not int or type(number2) is not int:
        raise ValueError("Introduce correct values")
    if number1 == 0 and number2 == 0:
        return -1
    if number1 == 0:
        return number2
    if number2 == 0:
        return number1


    if number1 == number2:
        return number1
    if number1 > number2:
        return gcd_recursive(number1 - number2, number2)
    else:
        return gcd_recursive(number1, number2 - number1)


def given_power(default_base, power):
    '''
    obtain a number
    :param default_base:
    :param power:
    :return:
    '''
    if type(default_base) is not int or type(power) is not int:
        raise ValueError("Introduce correct values")
    if power == 0:
        return 1
    if power == 1:
        return default_base
    if power > 1:
        return default_base * given_power(default_base, power - 1)
