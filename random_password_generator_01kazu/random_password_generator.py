import numpy as np
import string
import secrets


def str_insert(string: str, pos: int, characters: str) -> str:
    """
    Inserts character into a string.

    Parameters
    ----------

    string: str
        The string that would be inserted.
    pos: int
        The position of the character to be inserted.
    characters: str
        The characters that would be inserted in `string`.

    Returns
    -------
    new_string: str
        string with inserted character.

    Examples
    --------
    Inserts "happy" into "happy birthday" at the sixth index.

    >>> str_insert("happy birthday", 6, "happy")
    happy happyday
    """
    new_string = ""
    for index, char in enumerate(string):
        if len(new_string) > index:
            continue
        if index == pos:
            new_string += characters
            continue
        new_string += char
    return new_string


def random_password_generator(num_of_characters: int = 8) -> str:
    """Creates a password of eight or more characters.

    Parameters
    ----------
    num_of_characters: int, default = 8
        The number of characters for the password.

    Returns
    -------
    str
        The password whose length is specified by `num_of_characters`

    Raises
    ------
    ValueError
        If `num_of_characters` is less than 8
    TypeError
        if int datatype is not used.

    Examples
    --------
    Generate a password of 10 characters.

    >>> random_password_generator(10)
    ]b=[K1o<H~
    """
    try:
        if num_of_characters < 8:
            raise ValueError("The number of characters have to be greater or equal to 8")
        characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(secrets.choice(characters) for i in range(num_of_characters))
    except TypeError:
        print("Please enter an integer which is greater or equal to 8.")


def random_password_generator_known_words(keyword: str, num_of_characters: int = 8) -> str:
    """Create a password that contains words or characters provided.

    Parameters
    ----------
    word : str,
        The word that should be included in the password.
    num_of_characters: int,
        The number of characters of the password.

    Returns
    -------
    str
        The password whose length is specified by `num_of_characters` and contains `word` in it.

    Example
    -------
    Generates a password of 8 characters with "hey" in it.

    >>> random_password_generator_known_words("hey", 8)
    4>heyb=w

    """
    password = random_password_generator(num_of_characters)
    index_limit = len(password) - len(keyword)  # the num of characters that won't raise the IndexError
    keyword_pos = np.random.randint(index_limit + 1)
    return str_insert(password, keyword_pos, keyword)


def main() -> None:
    password = random_password_generator(10)
    password_known = random_password_generator_known_words("hey", 8)
    # print(f"Your New Password is {password}")
    print(f"Your New Password is {password}" if password else "")
    print(f"Your New Known Password is {password_known}" if password else "")
    print(str_insert("happy birthday", 6, "happy"))


if __name__ == "__main__":
    main()
