"""
演示函数基础定义练习案例：自动查核酸
"""

# 定义函数
def check():
    # 编写函数体输出信息
    print("欢迎来到黑马程序员！\n请出示您的健康码以及72小时核酸证明！")

# 调用函数
check()

def my_len(data):
    count = 0
    for i in data:
        count += 1
    return count

str1 = 'I Love You, GeJingyi'
print(my_len(str1))