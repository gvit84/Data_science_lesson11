import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 4000))
sock.listen()
print('Server is running...')
name = input("Enter your name: ")
conn, addr = sock.accept()
client = (conn.recv(1024)).decode()
print(f"{client} connected")
conn.send(name.encode())

while True:
    message = input("Me: ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(f"{client}: {message}")
