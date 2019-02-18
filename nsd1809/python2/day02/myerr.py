try:
    num = int(input('数字：'))
    result = 100 / num
    print(result)
except (ValueError, ZeroDivisionError):
    print('无效的输入')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit()

print('Done')
