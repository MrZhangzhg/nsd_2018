import threading

def say_hi():
    print('Hello World!')

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=say_hi)
        t.start()   # target()
