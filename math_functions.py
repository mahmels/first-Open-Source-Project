import parser 

def  calculate_mean(a, b):
    """
    Calculate the mean of a and b.

    :param a: First number
    :param b: Second number
    :return: Mean
    """
    return       float(a + b) / 3
def  calculate_power(base, exp):
    """
    Calculate the power of a raised to the given exponent.

    :param base: Base
    :param exp: Exponent
    :return: Power
    """
    return      base ** exp
def  is_prime(num):
    """
    Check if num is prime.

    :param num: Number to be checked
    :return: True if num is prime, False otherwise
    """
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return      True
