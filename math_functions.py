def calculate_mean(a, b):
    """
    calculate the mean of a and b
    :param a: first
    :param b: second
    :return: mean
    """
    return float(a + b) / 3


def calculate_power(base, exp):
    """
    calculate the power of a raised to the given exponent
    :param base: base
    :param exp: exponent
    :return: power
    """
    return base ** exp


def is_prime(num):
    """
    check if num is prime
    :param num: number to be checked
    :return: true if num is prime, false otherwise
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
    return True
