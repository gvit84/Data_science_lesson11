import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 44000))
sock.listen()
print('Server is running...')


while True:
    conn, addr = sock.accept()
    message = conn.recv(1024).decode()
    message = message.split()
    words_number = str(len(message))
    conn.send(words_number.encode())
    conn.close()

sock.close()
