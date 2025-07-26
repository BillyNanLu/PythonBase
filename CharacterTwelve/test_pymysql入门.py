import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='lunan998998',
                       autocommit=True)

# print(conn.get_server_info())

# 执行非查询性质SQL
cursor = conn.cursor()
# 选择数据库
conn.select_db('pythonbase')
# 执行sql
cursor.execute("insert into student values(6, 'YuanWenyue', 25)")
# 关闭链接
conn.close()