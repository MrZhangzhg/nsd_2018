from random import randint

def func1(n):
    return n % 2

def func2(n):
    return n + 1

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)   # [2, 88, 32, 12, 30, 45, 11, 51, 77, 19]
    print(list(filter(func1, nums)))
    print(list(filter(lambda n: n % 2, nums)))
    print('#' * 20)
    print(list(map(func2, nums)))
    print(list(map(lambda n: n + 1, nums)))
