from typing import List


# def quick_sort(numbers: List[int]) -> List[int]:


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(bucket_sort(nums))
