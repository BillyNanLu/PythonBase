import socket

socket_server = socket.socket()
socket_server.bind(("localhost", 8888))
socket_server.listen()
conn, address = socket_server.accept()

print(f"接收到了客户端的链接，客户端的信息是：{address}")

while True:
    data: str = conn.recv(1024).decode("UTF-8")
    print(f"客户端发来的消息是：{data}")
    msg = input("请输入你要和客户端回复的消息：")
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))

conn.close()
socket_server.close()