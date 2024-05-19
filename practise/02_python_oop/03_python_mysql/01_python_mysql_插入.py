
from pymysql import Connection

conn = Connection(
    host="localhost",
    port=2206,
    user="root",
    password=123456,
    autocommit=True,     # 设置自动提交, 设置后就不用再手动提交
    database="world"     # 选择要使用的数据库
)

# conn.select_db("world")

cursor = conn.cursor()
cursor.execute("insert into student values(10001, '周杰伦', 31, '男')")

# 通过commit确认
# conn.commit()

# 不关闭会占用数据库的衔接
conn.close()
