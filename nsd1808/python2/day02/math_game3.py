import random

def exam():
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [random.randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)   # 降序
    op = random.choice('+-')   # 随机选出+号或-号
    result = cmds[op](*nums)
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])   # 算式
    counter = 0

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:   # 不推荐，可以捕获所有异常
            print()
            continue
        if answer == result:
            print('Very Good!')
            break
        print('Wrong Answer!')
        counter += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    while True:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
