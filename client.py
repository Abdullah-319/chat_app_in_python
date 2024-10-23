import socket
import threading

def receive_messages(client_socket):
    """Receive messages from the server and print them."""
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(message.decode('utf-8'))
        except:
            break

def send_messages(client_socket):
    """Send messages to the server."""
    while True:
        message = input("")
        if message.lower() == 'exit':
            client_socket.send(message.encode('utf-8'))
            break
        client_socket.send(message.encode('utf-8'))

def main():
    host = '127.0.0.1'
    port = 2023

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Ask for username
    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))

    # Start threads for receiving and sending messages
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    send_messages(client_socket)

    client_socket.close()

if __name__ == "__main__":
    main()
