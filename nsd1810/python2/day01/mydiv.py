try:
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('无效的输入')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit(1)
else:     # 不发生异常才执行
    print(result)
finally:   # 不管异常是否发生，都会执行
    print('Done')
