import pymysql

# 创建连接
connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database="databasedemo"
)

# 创建游标
cur = connection.cursor()

# 准备sql语句
# sql = "INSERT INTO men(name, age, address) VALUES ('里昂', '28', '美国')"
sql = """
    INSERT INTO men(name, age, address) 
    VALUES
        ('John Doe', 30, '123 Main St'),
        ('Alice Smith', 25, '456 Elm Ave'),
        ('Michael Johnson', 40, '789 Oak Rd'),
        ('Emily Brown', 22, '567 Pine Ln'),
        ('David Lee', 28, '321 Maple Dr'),
        ('Sophia Garcia', 35, '987 Birch Ct'),
        ('Daniel White', 33, '654 Cedar Rd'),
        ('Olivia Martinez', 29, '890 Walnut Ave'),
        ('William Taylor', 27, '234 Spruce Ln'),
        ('Emma Harris', 31, '432 Cherry St');
"""
# 执行sql语句
cur.execute(sql)

# 提交事务
connection.commit()
# 仅查询不需要提交
connection.close()
