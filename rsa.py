'''
RSA is an encryption method that uses two keys: a public key 
for encryption and a private key for decryption. Here's how it works:

Key Generation:

Choose two large prime numbers, multiply them to get a value called N.
From this, calculate two keys: a public key (used to encrypt) and
 a private key (used to decrypt).

Encryption:

Using the public key, you convert (encrypt) your message into a 
coded form called ciphertext. This keeps the message secret.

Decryption:

Using the private key, you convert (decrypt) the ciphertext back into
 the original message.
The public key is shared with everyone, but only the person 
with the private key can decrypt the message. This makes RSA secure for sending sensitive information.
'''

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair
keyPair = RSA.generate(1024)  # 1024-bit key
pubKey = keyPair.publickey()   # Public key

# Display public key
print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print("Public Key in PEM format:")
print(pubKeyPEM.decode('ascii'))

# Display private key
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print("Private Key in PEM format:")
print(privKeyPEM.decode('ascii'))

# Encryption process
msg = 'Ismile Academy'  # Plaintext message
encryptor = PKCS1_OAEP.new(pubKey)  # Initialize the encryptor with the public key
encrypted = encryptor.encrypt(msg.encode('utf-8'))  # Encrypt the message
print("Encrypted:", binascii.hexlify(encrypted))  # Display encrypted message in hexadecimal

# Decryption process
decryptor = PKCS1_OAEP.new(keyPair)  # Initialize the decryptor with the private key
decrypted = decryptor.decrypt(encrypted)  # Decrypt the message
print("Decrypted:", decrypted.decode('utf-8'))  # Display the original message
