try:
    num = int(input('数字：'))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('无效的输入')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit()
else:       # 不发生异常才执行
    print(result)
finally:    # 不管异常是否发生，都会执行
    print('Done')

# 常用的组合是try-except和try-finally
