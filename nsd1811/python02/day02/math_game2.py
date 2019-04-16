from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    cmds = {'+': add, '-': sub}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列，默认升序
    op = choice('+-')
    result = cmds[op](*nums)   # 将列表拆开
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])  # 算式
    counter = 0

    while counter < 3:
        answer = int(input(prompt))
        if answer == result:
            print('Very good!!!')
            break

        print('不对哦')
        counter += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    while True:
        exam()
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
