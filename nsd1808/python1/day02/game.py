import random

computer = random.choice(['石头', '剪刀', '布'])
player = input('请出拳(石头/剪刀/布): ')

print('你出拳: %s， 计算机出拳: %s' % (player, computer))
if player == '石头':
    if computer == '石头':
        print('\033[32;1m平局\033[0m')
    elif computer == '剪刀':
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        print('\033[31;1mYou LOSE!!!\033[0m')
elif player == '剪刀':
    if computer == '石头':
        print('\033[31;1mYou LOSE!!!\033[0m')
    elif computer == '剪刀':
        print('\033[32;1m平局\033[0m')
    else:
        print('\033[31;1mYou WIN!!!\033[0m')
else:
    if computer == '石头':
        print('\033[31;1mYou WIN!!!\033[0m')
    elif computer == '剪刀':
        print('\033[31;1mYou LOSE!!!\033[0m')
    else:
        print('\033[32;1m平局\033[0m')

