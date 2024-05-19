"""
文件编码：
    UTF-8(是目前全球通用的编码格式)、GBK、Big5、等

文件的读取:
    打开,  open 函数, 打开已经存在的文件 或 新创建一个新文件
        open(name, mode, encoding)
            name：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。
            mode：设置打开文件的模式(访问模式)：r（只读）、写入（w）、追加(a)等。
                r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
                w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，原有内容会被删除。如果该文件不存在，创建新文件。
                a	打开一个文件用于追加。如果该文件已存在，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
            encoding:编码格式（推荐使用UTF-8）
    读取
        read(num)
            num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据。
        readlines()
            readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素。
        readline()
            一次读取一行内容
    关闭
        close()
            也就是关闭对文件的占用, 如果不调用close,同时程序没有停止运行，那么这个文件将一直被Python程序占用。

    with open 语法, 通过在with open的语句块中对文件进行操作,可以在操作完成后自动关闭close文件，避免遗忘掉close方法
        with open("python.txt", "r") as f:
            f.readlines()
"""


# 打开一个已存在的文件
import time

f = open("main.py", "r", encoding="UTF-8")      # 文件如果不写路径，表示和当前这个python文件内在同一目录, encoding不是在第三个参数, 所以这里使用关键字传参
print(f"读取10个字节的结果是: {f.read(10)}")
print(f"读取全部字节的结果是: {f.read()}")        # 注意: 这次调用read会从上次调用read的结尾处开始读取

print("------------------------------------------------------------")

f.seek(0, 0)                                    # seek可以将指针恢复到初始位置
print(f"读取全部字节的结果是: {f.read()}")

print("------------------------------------------------------------")

f.seek(0, 0)
lines = f.readlines()                           # 读取文件的全部行,封装到列表中
print(f"lines的结果是: {lines}, 类型是: {type(lines)}")

print("------------------------------------------------------------")

f.seek(0, 0)
line_1 = f.readline()
print(f"line_1的内容是: {line_1}")
line_2 = f.readline()
print(f"line_2的内容是: {line_2}")

print("------------------------------------------------------------")

f.seek(0, 0)
for line in f:
    print(f"每一行的数据为 {line}")

print("------------------------------------------------------------")

# time.sleep(10)                  # 程序睡眠
f.close()

print("------------------------------------------------------------")

with open("main.py", "r", encoding="UTF-8") as file:
    for line in file:
        print(f"每一行的数据为 {line}")


"""
文件的写入:
    函数:
        write()
            直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
        flush()
            当调用flush的时候，内容会真正写入文件,这样做是避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写磁盘）
    写操作注意:
        文件如果不存在，使用”w”模式，会创建新文件
        文件如果存在，使用”w”模式，会将原有内容清空
"""
# 打开一个不存在的文件
f = open("w_non-exist.txt", "w", encoding="UTF-8")
f.write("测试open的w模式")
# f.flush()
f.close()                       # close() 方法内置了flush 功能

# 打开一个存在的文件
f2 = open("w_exist.txt", "w", encoding="UTF-8")
f2.write("测试open的w模式")
f.close()


"""
文件的追加
    a模式，文件不存在会创建文件
    a模式，文件存在会在最后，追加写入文件
"""
# 打开一个不存在的文件
f = open("a_non-exist.txt", "a", encoding="UTF-8")
f.write("测试open的a模式")
# f.flush()
f.close()                           # close() 方法内置了flush 功能

# 打开一个存在的文件
f2 = open("a_exist.txt", "a", encoding="UTF-8")
f2.write("测试open的a模式")          # 即使不调用 flush() 或 close() 函数, 在程序运行完成时也会自动调用 close() 函数来解除对文件的占用
f.close()                           # 为了规范,还是应该显示调用. 正常的程序打开时会一直运行,如果不调用 f.close(), 文件就会一直被占用
