'''
Digital Signature and RSA Algorithm (In Short)

Digital Signature:
A digital signature ensures that a message is authentic (comes from
 the real sender) and hasn't been altered (integrity).
It uses asymmetric encryption, which means the sender has a 
private key (used to sign the message), and the recipient uses the
 public key (to verify the message).
It's commonly used in secure communication like email, contracts, 
and transactions.

RSA Algorithm:
RSA (Rivest-Shamir-Adleman) is a widely used asymmetric encryption algorithm based on the difficulty of factoring large prime numbers.
RSA generates a public key for encryption and verification and a private key for decryption and signing.
Digital Signature Process:
1. Generation:
The sender creates a hash (a short, fixed-length summary) of the message using a function like SHA-256.
The sender signs this hash using their private key to create a digital signature.
2. Verification:
The recipient uses the sender’s public key to verify the signature.
They compute the hash of the received message and compare it to the signed hash. If they match, the message is authentic and unaltered.

'''
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

def generate_signature(private_key, message):
    key = RSA.import_key(private_key)
    hashed_message = SHA256.new(message.encode())
    return pkcs1_15.new(key).sign(hashed_message)

def verify_signature(public_key, message, signature):
    key = RSA.import_key(public_key)
    hashed_message = SHA256.new(message.encode())
    try:
        pkcs1_15.new(key).verify(hashed_message, signature)
        return True
    except (ValueError, TypeError):
        return False

# Generate RSA key pair
key_pair = RSA.generate(2048)
public_key = key_pair.publickey().export_key()
private_key = key_pair.export_key()

# Example usage
message = "Hello, World!"
signature = generate_signature(private_key, message)
print("Generated Signature:", signature)

is_valid = verify_signature(public_key, message, signature)
print("Signature Verification Result:", is_valid)

