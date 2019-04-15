try:   # 把有可能发生异常的代码放到try中执行
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError):  # 用except捕获异常
    print('无效的数字')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit()  # 程序序到exit就会退出，后续代码不再执行
else:   # 没有发生异常才执行的语句
    print(result)
finally:  # 不管是否发生异常，都会执行的语句
    print('Done')
