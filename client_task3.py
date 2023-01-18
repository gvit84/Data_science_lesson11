import socket

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 44000))
    send_message = input("Enter the phrase: ")
    sock.send(send_message.encode())
    message = sock.recv(1024).decode()
    print(f"Number of words in the phrase is: {message}")

sock.close()