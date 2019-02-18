import random

def exam():
    nums = [random.randint(1, 100) for i in range(2)]  # 生成两个数字
    nums.sort(reverse=True)  # 降序排列
    op = random.choice('+-')
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('Very good')
    else:
        print('Wrong answer')

def main():
    while True:
        exam()
        # 将用户输入的内容去除两端空白字符后，取出第一个字符
        yn = input('Contine(y/n)? ').strip()[0]
        if yn in 'nN':  # 只有第一个字符是n或N才结束
            print('\nByebye')
            break

if __name__ == '__main__':
    main()
