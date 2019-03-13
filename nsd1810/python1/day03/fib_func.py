def gen_fib():
    fib = [0, 1]

    num = int(input('数列长度: '))
    for i in range(num - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

nums = gen_fib()
nums2 = [i * 2 for i in nums]
print(nums2)
