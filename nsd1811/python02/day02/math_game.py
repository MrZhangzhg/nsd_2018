from random import randint, choice

def exam():
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列，默认升序
    op = choice('+-')
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    prompt = '%s %s %s = ' % (nums[0], op, nums[1])  # 算式
    answer = int(input(prompt))
    if answer == result:
        print('Very good!!!')
    else:
        print('不对哦')

def main():
    while True:
        exam()
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
