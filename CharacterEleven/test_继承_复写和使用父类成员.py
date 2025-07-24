class Phone15:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("使用5g网络进行通话")

class Phone16(Phone15):
    IMEI = "ITCAST"
    producer = "新厂商：Apple"
    def call_by_5g(self):
        print("新增：开启CPU单核模式，确保通话的时候省电")
        super().call_by_5g()
        print("新增：关闭CPU单核模式，确保性能")

phone = Phone16()
phone.call_by_5g()
print(phone.producer)
