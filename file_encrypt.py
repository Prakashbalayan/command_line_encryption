import argparse
from cryptography.fernet import Fernet
import base64
import hashlib
import os

def generate_key(password):
    # Derive a 32-byte key from the password using SHA-256
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_file(file_path, key):
    # Read file content
    with open(file_path, 'rb') as f:
        data = f.read()

    # Encrypt the data
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    # Save encrypted data with .enc extension
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)

    print(f"File encrypted successfully: {encrypted_file_path}")

def main():
    parser = argparse.ArgumentParser(description='Encrypt a file using AES (via Fernet)')
    parser.add_argument('--file', required=True, help='Path to the input file')
    parser.add_argument('--algorithm', required=True, choices=['AES'], help='Encryption algorithm (Only AES supported)')
    parser.add_argument('--key', required=True, help='Secret key/password for encryption')

    args = parser.parse_args()

    # Only AES is supported here (Fernet uses AES-128 under the hood)
    if args.algorithm != 'AES':
        print("Only AES encryption is supported at the moment.")
        return

    key = generate_key(args.key)
    encrypt_file(args.file, key)

if __name__ == '__main__':
    main()
