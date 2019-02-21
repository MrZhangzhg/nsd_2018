import time

result = 0
start = time.time()
for i in range(10000000):
    result += i
print(result)
end = time.time()
print(end - start)
