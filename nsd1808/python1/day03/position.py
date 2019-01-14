import sys   # 导入sys模块

print(sys.argv)    # argv是sys模块中的列表，用于存储位置参数

for i in range(len(sys.argv)):
    print(sys.argv[i])

# python3 position.py hello 123
