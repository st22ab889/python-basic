"""
首先在数据库用用如下语句创建数据库以及表:
    create database py_sql charset utf8;
    use py_sql;
    create table orders(
        order_date date,
        order_id varchar(255),
        money int,
        province varchar(10)
    );
"""

from pymysql import Connection
from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record


text_file_reader = TextFileReader("./2011年1月销售数据.txt")
json_file_reader = JsonFileReader("./2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将2个月份的数据合并为1个list
all_data: list[Record] = jan_data + feb_data


conn = Connection(
    host="localhost",
    port=2206,
    user="root",
    password=123456,
    autocommit=True
)

cursor = conn.cursor()
conn.select_db("py_sql")

for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) " \
            f"values ('{record.date}', '{record.order_id}', '{record.money}', '{record.province}')"
    print(sql)
    cursor.execute(sql)

conn.close()
