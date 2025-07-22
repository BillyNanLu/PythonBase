import random as rnd

money = 10000
total_employees = 20  # 总员工数

for i in range(1, total_employees + 1):
    if money - 1000 > 0:
        random_num = rnd.randint(1, 10)
        if random_num < 5:
            print(f"第{i}位员工，绩效分为：{random_num}，低于5分，不发工资")
        else:
            print(f"第{i}位员工，绩效分为：{random_num}，发放工资：1000元")
            money -= 1000
    else:
        remaining = total_employees - (i - 1)  # 计算剩余员工数
        print(f"没钱了，剩下的{remaining}位员工工资下个月再说")
        break
