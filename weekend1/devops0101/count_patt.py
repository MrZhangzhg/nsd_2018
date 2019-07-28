import re

def count_patt(fname, patt):
    result = {}  # 结果保存到字典中
    # 正则表达式模式先编译，以获取更好的效率
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:   # 如果匹配到结果了
                key = m.group()
                result[key] = result.get(key, 0) + 1

    return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1234.5678.1.123456 1.23.123.28
    br = 'Chrome|Firefox|MSIE'
    print(count_patt(fname, ip))
    print(count_patt(fname, br))
