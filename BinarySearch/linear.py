from typing import List


def linear_search(numbers: List[int], value: int) -> int:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1


if __name__ == '__main__':
    num = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    print(linear_search(num, 15))
