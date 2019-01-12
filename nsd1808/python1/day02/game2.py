import random

all_choice = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]  # 人赢的情况
prompt = """(0) 石头
(1) 剪刀
(2) 布
Please input your choice(0/1/2): """   # 屏幕提示先定义成变量

computer = random.choice(all_choice)
ind = int(input(prompt))   # 用户输入列表的下标
player = all_choice[ind]   # 通过下标取出对应的元素

print('你出拳: %s， 计算机出拳: %s' % (player, computer))
if player == computer:
    print('\033[32;1m平局\033[0m')
elif [player, computer] in win_list:   # 人机选择的小列表是大列表的一项
    print('\033[31;1mYou WIN!!!\033[0m')
else:
    print('\033[31;1mYou LOSE!!!\033[0m')
