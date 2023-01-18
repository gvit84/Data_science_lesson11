import socket

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 5000))
    greeting_bot = (sock.recv(1024)).decode()
    print(greeting_bot)
    send_message = input("Make your choice: ").upper()
    sock.send(send_message.encode())
    message = sock.recv(1024).decode()
    print(f"Chat-bot answer: {message}")

sock.close()




