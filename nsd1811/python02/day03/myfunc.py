def func1(x):
    if x == 1:
        return 1

    return x * func1(x - 1)
    # 5 x func(4)
    # 5 x 4 x func(3)

if __name__ == '__main__':
    print(func1(5))
