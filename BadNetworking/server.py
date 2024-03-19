import socket
from threading import Thread
from messageProtocol import SecureMessageProtocol

MESSAGE_SIZE = 2048

server_private_key_path = "serverr_private_key.pem"
server_public_key_path = "serverr_public_key.pem"

server_private_key = SecureMessageProtocol.loadPrivateKeyfromPath(server_private_key_path)
server_public_key = SecureMessageProtocol.loadPublicKeyfromPath(server_public_key_path)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.1.232', 36973)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("Server is listening on {}:{}".format(*server_address))
    
    while True:
        connection, client_address = server_socket.accept()
        print("Connection from", client_address)
        client_handler = Thread(target=handle_client, args=(connection, client_address))
        client_handler.start()

def handle_client(connection, client_address):
    authenticated = False
    print("Connection from", client_address)
    try:
        server_public_key_string = SecureMessageProtocol.getReadablePublicKey(server_public_key)
        connection.send(server_public_key_string.encode())

        client_public_key_string = connection.recv(MESSAGE_SIZE).decode()
        print(client_public_key_string)
        client_public_key = SecureMessageProtocol.loadPublicKeyfromString(client_public_key_string)
        while True:
            buffer = connection.recv(MESSAGE_SIZE)
            command = SecureMessageProtocol.decrypt(buffer, server_private_key)
            command_string = str(command)

            commands = command_string.split(" ")
            match commands[0].lower():
                case "exit":
                    break
                case "authenticate":
                    if commands[1] == "S3cr3tP4ssw0rd_F0r_4uth3nt1c4t10n_1n_S3I_24":
                        connection.send(SecureMessageProtocol.encrypt("You are authenticated!".encode(), client_public_key))
                        authenticated = True
                    else:
                        connection.send(SecureMessageProtocol.encrypt("Wrong password!".encode(), client_public_key))
                case "getflag":
                    if authenticated:
                        connection.send(SecureMessageProtocol.encrypt("The flag is:\nSEI{k3y_n0t_pr1v4t3_4nym0r3}".encode(), client_public_key))
                    else:
                        connection.send(SecureMessageProtocol.encrypt("You are not authenticated!".encode(), client_public_key))
                case "help":
                    connection.send(SecureMessageProtocol.encrypt("Available commands:\nauthenticate <password>\ngetflag\nexit\nhelp".encode(), client_public_key))
                case _:
                    connection.send(SecureMessageProtocol.encrypt("Unknown command!".encode(), client_public_key))

    finally:
        connection.close()

if __name__ == "__main__":
    main()