class Vendor:
    def __init__(self, ph):
        self.phone = ph

class Bear:
    def __init__(self, color, size, phone):
        self.color = color  # 把属性绑定到具体的实例
        self.size = size
        self.vendor = Vendor(phone)

    def sing(self):
        print("My color is %s, Lalala" % self.color)

if __name__ == '__main__':
    bear1 = Bear('Brown', 'Large', '400-123-5678')
    print(bear1.vendor.phone)
    v1 = Vendor('400-111-2222')
    print(v1.phone)
