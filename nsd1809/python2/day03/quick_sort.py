from random import randint

def qsort(seq):
    """
    将第一个数假设为中间值，比它小的放到小列表，大的放到大列表，再把这三项
    拼接起来。小列表、大列表仍然要用同样的方法继承排序
    """
    if len(seq) < 2:
        return seq   # 如果列表只有一项或是空的，不需要排序，直接返回

    middle = seq[0]
    smaller = []
    larger = []
    for item in seq[1:]:
        if item < middle:
            smaller.append(item)
        else:
            larger.append(item)
    return qsort(smaller) + [middle] + qsort(larger)


if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
