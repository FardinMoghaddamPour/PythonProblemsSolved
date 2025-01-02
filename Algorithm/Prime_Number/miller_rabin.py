import random
import timeit

dice = random.SystemRandom()


def single_test(input_number: int, witness: int) -> bool:
    exponent = input_number - 1
    while not exponent & 1:
        exponent >>= 1

    if pow(witness, exponent, input_number) == 1:
        return True

    while exponent < input_number - 1:
        if pow(witness, exponent, input_number) == input_number - 1:
            return True

        exponent <<= 1

    return False


def miller_rabin_prime_number_check(input_number: int, iteration: int = 40) -> (bool | str):
    if not isinstance(input_number, int):
        return "Type Error you must enter an integer."
    if input_number < 2 or (input_number % 2 == 0 and input_number != 2):
        return False
    if input_number in (2, 3):
        return True
    for _ in range(iteration):
        witness = dice.randrange(2, input_number-1)
        if not single_test(input_number, witness):
            return False
    return True


start = timeit.default_timer()
print(miller_rabin_prime_number_check(2305843009213693951))
print(timeit.default_timer() - start)
