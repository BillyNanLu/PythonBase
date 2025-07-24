class Student1:
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")

student1 = Student1("GeJingyi", "22", "15812345678")
print(student1.name)
print(student1.age)
print(student1.tel)


class Student2:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

for i in range(1, 11):
    print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    address = input("请输入学生地址：")
    student2 = Student2(name, age, address)
    print(f"学生{i}信息录入完成，信息为：【学生姓名：{student2.name}，年龄：{student2.age}，地址：{student2.address}】")
