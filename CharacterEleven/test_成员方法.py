class Student:
    name = None

    def say_hello(self):
        print(f"大家好呀，我是{self.name}，欢迎大家多多关照")

    def say_hi(self, msg):
        print(f"大家好，我是：{self.name}，{msg}")

stu = Student()
stu.name = "周杰轮"
stu.say_hi("哎哟不错哟")

stu2 = Student()
stu2.name = "林俊节"
stu2.say_hi("小伙子我看好你")