import random

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    cmds = {'+': add, '-': sub}
    nums = [random.randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    op = random.choice('+-')
    prompt = '%s%s%s=' % (nums[0], op, nums[1])
    result = cmds[op](*nums)
    # if op == '+':
    #     result = nums[0] + nums[1]
    # else:
    #     result = nums[0] - nums[1]
    tries = 0
    while tries < 3:
        try:
            answer = int(input(prompt))
        except:
            print()
            continue
        if answer == result:
            print('Very Good!!!')
            break
        else:
            print('答错了')
        tries += 1
    else:
        print('%s%s' % (prompt, result))

if __name__ == '__main__':
    while True:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'Nn':
            print('\nBye-bye')
            break
