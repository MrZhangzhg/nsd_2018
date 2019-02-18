import random

def exam():
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [random.randint(1, 100) for i in range(2)]  # 生成两个数字
    nums.sort(reverse=True)  # 降序排列
    op = random.choice('+-')
    result = cmds[op](*nums)
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    counter = 0

    while counter <= 2:
        try:
            answer = int(input(prompt))
        except:     # 空except语句，可以捕获所有异常，但是不推荐
            print() # 打印回车
            continue

        if answer == result:
            print('Very good')
            break
        print('Wrong answer')
        counter += 1
    else:   # 循环正常结束，没有被break才执行的语句
        print('%s%s' % (prompt, result))

def main():
    while True:
        exam()
        # 将用户输入的内容去除两端空白字符后，取出第一个字符
        try:
            yn = input('Contine(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'    # 如果按了ctrl+c/d，算用户回答了n

        if yn in 'nN':  # 只有第一个字符是n或N才结束
            print('\nByebye')
            break

if __name__ == '__main__':
    main()
