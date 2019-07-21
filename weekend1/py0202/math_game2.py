from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    cmds = {'+': add, '-': sub}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    op = choice('+-')  # 随机选择+-号

    # 计算出正确答案
    result = cmds[op](*nums)

    # 算式
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])

    # 判断对错
    counter = 0
    while counter < 3:
        # 让用户做答
        try:
            answer = int(input(prompt))
        except:  # 不指定具体的异常，可以捕获所有异常，但是不推荐
            print()
            continue

        if answer == result:
            print('Very Good!!!')
            break

        print('Wrong!!!')
        counter += 1
    else:  # 循环被break则不执行，否则执行
        print('%s%s' % (prompt, result))

def main():
    while True:
        exam()
        # 去除用户输入的额外空格，并取出第一个字符
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            yn = 'y'
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break



if __name__ == '__main__':
    main()
