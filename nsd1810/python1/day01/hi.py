# if 3 > 0:
#     print('ok')
#     print('yes')
#
# print('done')
############################
# print('Hello World!')
# print('hao', 123)   # 默认各项间用空格分开
# print('hao', 123, 'abc', sep='***')   # 指定各项之间的分隔符
# print('hao' + 123)   # 不能把字符和数字相加，报错
# print('hao' + '123')   # 现在的123是字符串
###############################
num = input('number: ')   # 赋值语句=两边的空格不强制，建议写上
print(num)   # 变量引用不用加$了
print('您输入了:', num)
# a = 5 + num   # input读入的数据一定是字符类型，数字和字符不能做四则运算，报错
a = 5 + int(num)   # int可以将字符形式的数字转换成整数数字
print(a)
