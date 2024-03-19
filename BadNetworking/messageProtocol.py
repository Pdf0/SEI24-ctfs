
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

MESSAGE_SIZE = 2048

class SecureMessageProtocol:
    def encrypt(message, public_key):
        encrypted_message = public_key.encrypt(
            message,
            padding.PKCS1v15()
        )
        return encrypted_message

    def decrypt(encrypted_message, private_key):
        decrypted_message = private_key.decrypt(
            encrypted_message,
            padding.PKCS1v15()
        )
    
        return decrypted_message.decode()

    def getReadablePublicKey(public_key):
        key = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        return key.decode()
    
    def getReadablePrivateKey(private_key):
        key = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        return key.decode()
    
    def loadPrivateKeyfromPath(private_key_path):
        with open(private_key_path, "rb") as private_key_fd:
            return serialization.load_pem_private_key(private_key_fd.read(), password=None)

    def loadPublicKeyfromPath(public_key_path):
        with open(public_key_path, "rb") as public_key_fd:
            return serialization.load_pem_public_key(public_key_fd.read())
    
    def loadPrivateKeyfromString(private_key_string):
        return serialization.load_pem_private_key(private_key_string.encode(), password=None)

    def loadPublicKeyfromString(public_key_string):
        return serialization.load_pem_public_key(public_key_string.encode())
