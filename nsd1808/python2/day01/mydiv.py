try:
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('Invalid input.')
except (KeyboardInterrupt, EOFError):
    print('end')
else:   # 不发生异常才执行
    print(result)
finally:   # 不管是否发生异常，都会执行
    print('Done')
