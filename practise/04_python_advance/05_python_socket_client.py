
import socket

# 创建Socket对象
socket_client = socket.socket()

# 连接到服务端
socket_client.connect(('localhost', 6688))

while True:
    msg = input("请输入要给服务端发送的消息：")
    if msg == 'exit':
        break

    # 发送消息
    socket_client.send(msg.encode('UTF-8'))

    # 接受返回消息. recv的参数是用来设置缓冲区大小,一般给1024即可. recv方法返回值是一个字节数组(也就是bytes对象),可以用decode方法通过UTF-8编码,将字节数组转换为字符串对象
    recv_data = socket_client.recv(1024)                        # recv 方法同样是阻塞方法, 如果没有接收到消息会一直阻塞在这里
    print(f"服务端返回的消息是：{recv_data.decode('UTF-8')}")

# 关闭连接
socket_client.close()

