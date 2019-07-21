# def foo():
#     print('in foo')
#     bar()
#
# def bar():
#     print('in bar')
#
# if __name__ == '__main__':
#     foo()

def func(n):
    if n == 1:
        return 1

    return n * func(n - 1)

if __name__ == '__main__':
    print(func(5))
