try:
    num = int(input('number: '))   # 把有可能发生异常的语句放到try中
    result = 100 / num
except (ValueError, ZeroDivisionError):   # 捕获异常
    print('无效输入，必须输入非0数字')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    # exit()
else:
    print(result)  # 异常不发生才执行的语句，放到else中
finally:
    print('DONE')   # 不管是否发生异常都要执行的语句，放到finally中

# try-except 和 try-finally这两种组合用得多
