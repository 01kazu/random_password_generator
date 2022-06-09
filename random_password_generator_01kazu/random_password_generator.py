import numpy as np
import string
import secrets


def random_password_generator(num_of_characters: int = 8) -> str:
    """Creates a password of eight or more characters.

    Parameters
    ----------
    num_of_characters: int, default = 8
        The number of characters of the password.

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
    Generates a password of

    >>> random_password_generator_known_words("hey", 8)
    4>heyb=w

    """
    password_known = ""
    password = random_password_generator(num_of_characters)
    index_limit = len(password) - len(keyword)  # the num of characters that won't raise the IndexError
    keyword_index = np.random.randint(index_limit + 1)
    for index, char in enumerate(password):
        if len(password_known) > index:  #
            continue
        if index == keyword_index:
            password_known += keyword
        password_known += char
    return password_known


def main() -> None:
    password = random_password_generator(10)
    password_known = random_password_generator_known_words("hey", 8)
    # print(f"Your New Password is {password}")
    print(f"Your New Password is {password}" if password else "")
    print(f"Your New Known Password is {password_known}" if password else "")


if __name__ == "__main__":
    main()
