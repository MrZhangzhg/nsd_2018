# print('Hello World!')
#
# if 3 > 10:
#     print('yes')
#     print('ok')
#
# if 3 > 0: print('abc')   # 无错误，不推荐
#################################################
#
# print('Hello World!')
# print('Hello', 'World!')
# print('Hello', 'World!', 10, sep='***')  # 定义各项之间的分隔符
# print('Hello' + 'World')
#################################################
#
number = input("number:")  # input读入的数据全部是字符类型
print(number)
print(int(number) + 10)   # int(number)将字符转成数字
print(number + '10')
print(number + str(10))   # str(10)把数字转成字符

