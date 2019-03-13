def gen_fib(num=10):
    fib = [0, 1]

    # num = int(input('数列长度: '))
    for i in range(num - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

# nums = gen_fib()
# nums2 = [i * 2 for i in nums]
# print(nums2)
nlist = [5, 8, 10]
for n in nlist:
    result = gen_fib(n)
    print(result)

l = int(input('数列长度: '))
print(gen_fib(l))

print(gen_fib())
