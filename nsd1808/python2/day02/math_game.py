import random

def exam():
    nums = [random.randint(1, 100) for i in range(2)]
    nums.sort()  # 默认升序排列
    nums.reverse()   # 反翻
    op = random.choice('+-')   # 随机选出+号或-号
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])   # 算式
    answer = int(input(prompt))
    if answer == result:
        print('Very Good!')
    else:
        print('Wrong Answer!')

def main():
    while True:
        exam()
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('Bye-bye')
            break

if __name__ == '__main__':
    main()
