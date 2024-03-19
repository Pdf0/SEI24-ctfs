import socket

from messageProtocol import SecureMessageProtocol

MESSAGE_SIZE = 2048


def main():
    server_address = ("93.108.101.115", 36973)
    client_private_key_path = 'private_key.pem'
    client_public_key_path = 'clientt_public_key.pem'

    client_private_key = SecureMessageProtocol.loadPrivateKeyfromPath(client_private_key_path)
    client_public_key = SecureMessageProtocol.loadPublicKeyfromPath(client_public_key_path)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.connect(server_address)
        print("Connected to {}:{}".format(*server_address))

        server_public_key_string = connection.recv(MESSAGE_SIZE).decode()
        print(server_public_key_string)
        server_public_key = SecureMessageProtocol.loadPublicKeyfromString(server_public_key_string)

        client_public_key_string = SecureMessageProtocol.getReadablePublicKey(client_public_key)
        connection.send(client_public_key_string.encode())

        while True:
            command = input("> ")
            connection.send(SecureMessageProtocol.encrypt(command.encode(), server_public_key))

            response = connection.recv(MESSAGE_SIZE)
            print(SecureMessageProtocol.decrypt(response, client_private_key))

if __name__ == "__main__":
    main()

