import time
from tqdm import tqdm

def deco(func):
    def timeit():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return timeit

@deco
def myadd():
    result = 0
    for i in tqdm(range(10000000)):
        result += i
    print(result)

if __name__ == '__main__':
    myadd()
