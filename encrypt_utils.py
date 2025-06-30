from cryptography.fernet import Fernet

# Generate and save a key (only run once and store securely)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt file data
def encrypt_data(data, key):
    return Fernet(key).encrypt(data)

# Decrypt file data
def decrypt_data(data, key):
    return Fernet(key).decrypt(data)
