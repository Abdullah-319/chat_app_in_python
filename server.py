import socket
import threading

clients = []  # List to hold connected clients
client_usernames = {}  # Dictionary to hold client sockets and their usernames

def handle_client(client_socket, username):
    """Handle communication with a connected client."""
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            
            # Decode and print the message on the server
            decoded_message = message.decode('utf-8')
            print(f"{username}: {decoded_message}")

            # Broadcast the message to all clients
            broadcast_message(f"{username}: {decoded_message}", client_socket)
        except:
            break

    # Remove client from the list and close the connection
    client_socket.close()
    clients.remove(client_socket)
    del client_usernames[client_socket]
    broadcast_message(f"{username} has left the chat.", None)

def broadcast_message(message, sender_socket):
    """Send a message to all connected clients except the sender."""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                # If the client cannot be reached, remove it
                client.close()
                clients.remove(client)

def start_server():
    """Start the chat server."""
    host = '127.0.0.1'
    port = 2023
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Ask for username
        client_socket.send("Enter your username: ".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8')

        clients.append(client_socket)
        client_usernames[client_socket] = username

        print(f"{username} has joined the chat.")
        broadcast_message(f"{username} has joined the chat.", None)

        # Start a new thread for handling this client
        threading.Thread(target=handle_client, args=(client_socket, username)).start()

if __name__ == "__main__":
    start_server()
