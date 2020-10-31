from typing import List


# def selection_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     index = 0
#     tmp = numbers[0]
#     for i in range(len_numbers):
#         tmp = numbers[i]
#         for j in range(i+1, len_numbers):
#             if tmp > numbers[j]:
#                 tmp = numbers[j]
#                 index = j
#         numbers[i], numbers[index] = numbers[index], numbers[i]
#     return numbers


def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i+1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


if __name__ == '__main__':
    import random
    num = [random.randint(0, 1000) for _ in range(10)]
    print(selection_sort(num))
