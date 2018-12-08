import random

all_choice = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请出拳(0/1/2): """
cwin = 0
pwin = 0

while cwin < 2 and pwin < 2:
    computer = random.choice(all_choice)
    index = int(input(prompt))
    player = all_choice[index]

    print('你的出拳:', player, ', 计算机出拳:', computer)
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')
