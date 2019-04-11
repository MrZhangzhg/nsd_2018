import random

all_choice = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): '''
computer = random.choice(all_choice)
ind = int(input(prompt))   # 将用户输入的字符转换为数字
player = all_choice[ind]   # 通过数字下标，取出列表中的字符串

print('你的选择是:%s, 计算机出拳: %s' % (player, computer))

if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win_list:
    print('\033[31;1mYou WIN!!!\033[0m')
else:
    print('\033[31;1mYou LOSE!!!\033[0m')
