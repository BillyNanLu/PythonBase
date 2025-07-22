"""
演示使用while和for循环遍历列表
"""


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    mylist = ["传智教育", "黑马程序员", "Python"]
    # 循环控制变量：通过下标索引来控制，默认0
    # 每一次循环将下标苏姚
    index = 0
    while index < len(mylist):
        print(mylist[index])
        index += 1

list_while_func()

print('-' * 50)

def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:
    """
    mylist = ["传智教育", "黑马程序员", "Python"]
    for i in mylist:
        print(i)

list_for_func()
