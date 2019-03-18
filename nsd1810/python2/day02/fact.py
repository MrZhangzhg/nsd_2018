def fact(n):
    if n == 1:
        return 1

    return n * fact(n - 1)

if __name__ == '__main__':
    print(fact(5))
    # fact(5) => 5 * fact(4) => 5 * 4 * fact(3) => 5 * 4 * 3 * fact(2)
