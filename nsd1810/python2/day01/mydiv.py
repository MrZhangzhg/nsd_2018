try:
    num = int(input('number: '))
    result = 100 / num
    print(result)
except (ValueError, ZeroDivisionError):
    print('无效的输入')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit(1)

print('Done')
