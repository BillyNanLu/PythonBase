"""
演示文件操作综合案例：文件备份
"""

# 打开文件得到文件对象，准备读取
fr = open('bill.txt', 'r', encoding='utf-8')
# 打开文件得到文件对象，准备写入
fw = open('bill.bak', 'w', encoding='utf-8')
# for循环读取文件
for line in fr:
    if line.strip().split(',')[4] == '测试':
        continue
    fw.write(line)
    fw.write("\n")

# close2个文件对象
fr.close()
fw.close()