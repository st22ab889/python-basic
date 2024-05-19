"""
DML(Data Manipulation Language)，数据操纵语言。适用范围：对数据库中的数据进行一些简单操作，如insert、delete、update、select等。
    DML操作是可以手动控制事务的开启、提交和回滚的。DDL操作是隐性提交的，不能rollback！
    DQL(data query language)，数据查询语言，专门用来查询数据
DDL(Data Definition Language)，数据定义语言。适用范围：对数据库中的某些对象（例如database、table）进行管理，如Create、Alter和Drop。
DCL(data control language)数据库控制语言。数据库控制语言，如commit，revoke之类的，在默认状态下，只有sysadmin,dbcreator,db_owner或db_securityadmin等人员才有权力执行DCL
"""


"""
在Python中，使用第三方库：pymysql 来完成对MySQL数据库的操作。安装：
    pip install pymysql
"""

from pymysql import Connection

conn = Connection(
    host="localhost",
    port=2206,
    user="root",
    password=123456
)

print(conn.get_server_info())

conn.select_db("test")

# 获取游标对象
cursor = conn.cursor()

# 运行非查询性质SQL
# cursor.execute("create table test_pymysql(id int)")

# 运行查询SQL
cursor.execute("select * from student")
results = cursor.fetchall()
print(results)  # 是个元组, 元组里面的元素又是元组
for r in results:
    print(r)

# 不关闭会占用数据库的衔接
conn.close()