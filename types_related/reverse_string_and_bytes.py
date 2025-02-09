from typing import Union


def reverse_string(input_string: Union[str, bytes]) -> Union[str, bytes]:

    """
    Reverses a string or byte sequence efficiently using slicing.

    Sample usage:
        sample_string = "Hello"
        result = reverse_string(sample_string)
        print(result)  # Output: "olleH"

        sample_bytes = b"Hello"
        result = reverse_string(sample_bytes)
        print(result)  # Output: b"olleH"

    :param input_string: A string or bytes to be reversed.
    :return: The reversed input, maintaining its original type.
    """

    if not isinstance(input_string, (str, bytes)):
        raise TypeError("Input must be a string or bytes")

    return input_string[::-1]


def reverse_string_using_for_loop(input_string: Union[str, bytes]) -> Union[str, bytes]:

    """
    Reverses a string or bytes using a pure for-loop.

    Sample usage:
        sample_string = "Hello"
        result = reverse_string_using_for_loop(sample_string)
        print(result)  # Output: "olleH"

    :param input_string: The string or bytes to be reversed.
    :return: The reversed string or bytes, maintaining the original type.
    """

    if not isinstance(input_string, (str, bytes)):
        raise TypeError("Input must be a string or bytes")

    reversed_content = b''.join(
        input_string[letter:letter + 1] for letter in range(
            len(input_string) - 1,
            -1,
            -1,
        )
    ) if isinstance(
        input_string,
        bytes,
    ) else ''.join(
        input_string[letter] for letter in range(
            len(input_string) - 1,
            -1,
            -1,
        )
    )

    return reversed_content
