from random import randint

def quick_sort(seq):
    if len(seq) < 2:
        return seq

    middle = seq[0]
    smaller = []
    larger = []

    for item in seq[1:]:
        if item < middle:
            smaller.append(item)
        else:
            larger.append(item)

    return quick_sort(smaller) + [middle] + quick_sort(larger)


if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(quick_sort(nums))
