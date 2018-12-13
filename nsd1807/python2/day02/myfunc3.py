def func1(n):
    if n == 1:
        return 1

    return n * func1(n - 1)
          # 5 * func(4)
          # 5 * 4 * func(3)

if __name__ == '__main__':
    print(func1(5))


