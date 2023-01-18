import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 5000))
sock.listen()
print('Server is running...')

while True:
    conn, addr = sock.accept()
    mes = "Choose a drink and I will make you it:\n1. Coffee\n2. Tea\n3. Capuccino\n4. Latte"
    conn.send(mes.encode())
    message = conn.recv(1024).decode()

    if message == 'COFFEE':
        answer = "You chose 'COFFEE'"
        conn.send(answer.encode())
    elif message == 'TEA':
        answer = "You chose 'TEA'"
        conn.send(answer.encode())
    elif message == 'CAPUCCINO':
        answer = "You chose 'CAPUCCINO'"
        conn.send(answer.encode())
    elif message == 'LATTE':
        answer = "You chose 'LATTE'"
        conn.send(answer.encode())
    else:
        a = 'we do not have such a drink'
        conn.send(a.encode())
    conn.close()

sock.close()

