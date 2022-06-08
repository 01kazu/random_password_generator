from ..random_password_generator import random_password_generator


def test_length_of_random_password():
    n = 10
    password_len = len(random_password_generator(n))
    assert n == password_len
