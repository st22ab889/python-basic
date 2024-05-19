# 字面量其实就是常量
6666
1.1111111
"ipaddress"

# 变量
money = 50
# print(内容1,内容2,内容3,...内容N)
print("多少钱:", money)

money = money - 20
print("还有多少钱:", money)


# type() 语句, 查看数据的类型. 注意：变量无类型，但是存储的数据有类型
print(type("牌神"))
print(type(20))
var_type = type(money)
print(var_type)


# 数据类型的转换，浮点数转整型会丢失精度
num_str = str(11)
print("数字转字符串:", num_str, ",type:",  type(num_str))

float_str = str(1.0011)
print("浮点数转字符串:", float_str, ",type:",  type(float_str))

num_int = int("100")
print("字符串转整型:", num_int, ",type:",  type(num_int))

num_int2 = int(100.123)
print("浮点数转整型:", num_int2, ",type:",  type(num_int2))

num_float = float("1.111")
print("字符串转浮点数:", num_float, ",type:",  type(num_float))


# 标识符只许出现英文、中文、数字、下划线，不能以数字开头;  大小写敏感; 不允许使用关键字.
# 变量命名规范： 当多个单词组合,使用下划线连接单词，不要使用驼峰命名; 英文字母要全部小写

# 算术运算符：+、-、*、/、//(取整除)、%(取余)、**(指数)
# 符合赋值运算符: +=、-=、*=、/=、//==、%==、**==
# 赋值运算符: =




