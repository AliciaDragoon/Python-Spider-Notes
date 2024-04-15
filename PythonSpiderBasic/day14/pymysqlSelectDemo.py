import pymysql
from pymysql.cursors import DictCursor

# 创建连接
connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database="databasedemo"
)

# 创建游标
# cur = connection.cursor()
cur = connection.cursor(DictCursor)

# 准备sql语句
sql = "select * from men"

# 执行sql语句
cur.execute(sql)

# 获取查询结果
one = cur.fetchone()
print(one)
another = cur.fetchone()
print(another)
# (1, '里昂', 28, '美国')
# (2, 'John Doe', 30, '123 Main St')
allone = cur.fetchall()
print(allone)
print(type(allone))
# <class 'tuple'>
# <class 'list'>

# 提交事务
# connection.commit()
# 仅查询不需要提交

# 断开连接
connection.close()
