"""
列表模拟栈结构
栈：是一个后进先出的结构
"""
def push_it():
    print('push')

def pop_it():
    print('pop')

def view_it():
    print('view')

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
