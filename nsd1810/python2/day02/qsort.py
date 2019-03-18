from random import randint

def qsort(seq):
    if len(seq) < 2:  # 列表只有一项或0项，不用排序，直接返回
        return seq

    middle = seq[0]   # 假设第一项是中间值
    smaller = []      # 比中间值小的列表
    larger = []       # 比中间值大的列表
    for item in seq[1:]:   # 遍历列表剩余项，数字分别放到两个列表中
        if item <= middle:
            smaller.append(item)
        else:
            larger.append(item)

    return qsort(smaller) + [middle] + qsort(larger)

if __name__ == '__main__':
    alist = [randint(1, 100) for i in range(10)]
    print(alist)
    print(qsort(alist))
