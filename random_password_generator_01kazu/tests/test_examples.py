from ..random_password_generator import (
    random_password_generator,
    random_password_generator_known_words,
    str_insert,
)


def test_length_of_random_password() -> None:
    n = 10
    password_len = len(random_password_generator(n))
    assert n == password_len


def test_length_of_random_password_known() -> None:
    word = "hello"
    password = random_password_generator_known_words(word, 10)
    assert word in password


def test_string_insert() -> None:
    string = "happy birthday"
    pos = 6
    characters = "dappy"
    replace_string = str_insert(string, pos, characters)
    assert characters == replace_string[6 : 6 + len(characters)]
