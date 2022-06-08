import string
import secrets


def random_password_generator(num_of_characters: int) -> str:
    """Creates a password of eight or more characters.

    Parameters
    ----------
    num_of_characters: int
        The number of characters of the password.

    Returns
    -------
    password: str
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
    if isinstance(num_of_characters, int):
        if num_of_characters < 8:
            raise ValueError("The number of characters have to be greater or equal to 8")
    else:
        raise TypeError("The arguments should be a number of type int")

    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for i in range(num_of_characters))


def main() -> None:
    password = random_password_generator(10)
    print(f"Your New Password is {password}")


if __name__ == "__main__":
    main()
