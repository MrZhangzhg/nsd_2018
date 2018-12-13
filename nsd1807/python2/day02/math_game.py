def exam():


if __name__ == '__main__':
    while True:
        exam()
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'Nn':
            print('\nBye-bye')
            break
