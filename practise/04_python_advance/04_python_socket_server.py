"""
socket (简称 套接字) 是进程之间通信一个工具，好比现实生活中的插座，所有的家用电器要想工作都是基于插座进行，进程之间想要进行网络通信需要socket。
Socket负责进程之间的网络数据传输，好比数据的搬运工。

2个进程之间通过Socket进行相互通讯，就必须有服务端和客户端
    Socket服务端：等待其它进程的连接、可接受发来的消息、可以回复消息
    Socket客户端：主动连接服务端、可以发送消息、可以接收回复
"""
import socket

# 创建Socket对象
socket_server = socket.socket()

# 绑定IP地址和端口
socket_server.bind(("localhost", 6688))

# 监听端口, 参数表示接受的连接数量
socket_server.listen(1)

# 等待客户端连接, 返回的是一个二元元组(二元元组就是一个元组里面只有2个元素)
result = socket_server.accept()             # accept()是一个阻塞的方法,等待客户端的连接,如果没有衔接就阻塞在一行,不向下运行
conn = result[0]                            # 客户端和服务端的连接对象
ipaddress = result[1]                       # 客户端的地址信息
# conn, ipaddress = socket_server.accept()  # 上面三行代码等同于这句代码

print(f"接受到了客户端的连接, 客户端的地址是:{ipaddress}")

while True:
    # 接受客户端信息, recv的参数是用来设置缓冲区大小,一般给1024即可. recv方法返回值是一个字节数组(也就是bytes对象),可以用decode方法通过UTF-8编码,将字节数组转换为字符串对象
    data: str = conn.recv(1024).decode("UTF-8")

    print(f"客户端发来的消息是: {data}")

    # 发送回复消息
    # msg = input("请输入你要回复客户端的消息：").encode("UTF-8")       # encode 可以将字符串编码为字节数组对象
    msg = input("请输入你要回复客户端的消息：")

    if msg == 'exit':
        break

    conn.send(msg.encode("UTF-8"))


# 关闭连接
conn.close()                # 关闭的是和客户端本次的通讯连接, 如果socket不关闭, 还可以继续调用accept, 等待客户端来连接
socket_server.close()       # 关闭的是整个socket

