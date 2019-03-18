from random import randint, choice

def exam():
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 默认升序，改为降序
    op = choice('+-')
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0]- nums[1]
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('Very Good!')
    else:
        print('Wrong Answer!')

def main():
    while True:
        exam()
        yn = input('Continue(y/n)? ').strip()[0]  # 取出用户输入的第一个非空字符
        if yn in 'nN':
            print('\nBye-bye')
            break


if __name__ == '__main__':
    main()
