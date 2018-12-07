import random

all_choice = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
computer = random.choice(all_choice)
player = input('请出拳(石头/剪刀/布): ')

print('你的出拳:', player, ', 计算机出拳:', computer)
if player == computer:
    print('平局')
elif [player, computer] in win_list:
    print('You WIN!!!')
else:
    print('You LOSE!!!')
