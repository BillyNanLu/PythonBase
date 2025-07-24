class phone1:
    __current_voltage = 0.8

    def __keep_single_core(self):
        if self.__current_voltage:
            print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核运行进行省电。")

phone1 = phone1()
phone1.call_by_5g()

print('-' * 80)

class phone2:
    def __init__(self, is_5g_enable=False):
        # 私有成员变量：5G开启状态
        self.__is_5g_enable = is_5g_enable

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

# 创建开启5G的手机实例
phone_with_5g = phone2(True)
phone_with_5g.call_by_5g()  # 测试5G通话
print("-----")
# 创建默认关闭5G的手机实例
phone_without_5g = phone2()
phone_without_5g.call_by_5g()  # 测试4G通话