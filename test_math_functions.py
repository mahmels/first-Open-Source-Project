from math_functions import calculate_mean, calculate_power, is_prime


def test_calculate_mean():
    assert calculate_mean(5, 7) == 6
    assert calculate_mean(2, 3) == 2.5
    assert calculate_mean(3, 9) == 6


def test_calculate_power():
    assert calculate_power(2, 4) == 16
    assert calculate_power(5, 2) == 25
    assert calculate_power(3, 7) == 2187


def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(7)
    assert not is_prime(8)

