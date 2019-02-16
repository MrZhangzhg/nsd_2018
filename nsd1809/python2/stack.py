"""
列表模拟栈结构
栈：是一个后进先出的结构
"""

stack = []

def push_it():
    data = input('data to push: ').strip()
    if data:    # 如果字符串非空
        stack.append(data)

def pop_it():
    if stack:   # 如果列表非空
        print('from stack, popped \033[31;1m%s\033[0m' % stack.pop())
    else:
        print('\033[31;1mEmpty stack\033[0m')

def view_it():
    print('\033[32;1m%s\033[0m' % stack)

def show_menu():
    prompt = """(0) push it
(1) pop it
(2) view it
(3) quit
Please input your choice(0/1/2/3): """
    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('Invalid choice. Try again.')
            continue
        if choice == '3':
            break
        if choice == '0':
            push_it()
        elif choice == '1':
            pop_it()
        else:
            view_it()


if __name__ == '__main__':
    show_menu()
