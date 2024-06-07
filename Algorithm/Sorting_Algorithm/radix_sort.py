from functools import reduce
from random import shuffle
import time


def flatten(nested_list):
    return reduce(lambda x, y: x + y, nested_list)


def get_num_digits(numbers):
    if not numbers:
        return 0
    max_number = max(numbers)
    return len(str(max_number))


def get_digit(number, digit_index):
    return number // 10 ** digit_index % 10


def radix_sort(numbers):
    num_digits = get_num_digits(numbers)
    for digit_index in range(num_digits):
        buckets = [[] for _ in range(10)]
        for number in numbers:
            digit = get_digit(number, digit_index)
            buckets[digit].append(number)
        numbers = flatten(buckets)
    return numbers


def main():
    sample_list = [55, 45, 3, 289, 213, 1, 288, 53, 2]

    start_time = time.time()
    sorted_sample_list = radix_sort(sample_list)
    end_time = time.time()
    print("Sorted sample list:", sorted_sample_list)
    print(f"Time taken to sort sample list: {end_time - start_time:.6f} seconds")

    large_list = [i for i in range(1000000)]
    shuffle(large_list)

    start_time = time.time()
    sorted_large_list = radix_sort(large_list)
    end_time = time.time()
    print("First 6 elements of sorted large list:", sorted_large_list[:6])
    print("Last 6 elements of sorted large list:", sorted_large_list[-6:])
    print(f"Time taken to sort large list: {end_time - start_time:.6f} seconds")


if __name__ == "__main__":
    main()
