from random import randint, choice

def exam():
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 默认升序，改为降序
    op = choice('+-')
    result = cmds[op](*nums)
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    counter = 0

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:
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
            yn = input('Continue(y/n)? ').strip()[0]  # 取出用户输入的第一个非空字符
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break


if __name__ == '__main__':
    main()
