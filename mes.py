'''
What is MAC?

MAC ensures that a message sent between two parties has not
 been tampered with and is authentic. It uses a secret key
and a cryptographic hash function to create a unique code (MAC)
 for the message. The receiver can check the MAC to ensure that
   the message is unchanged and genuine.

How MAC Works:
Sender's Side:

The sender combines the message with a secret key and applies a
 hash function (like MD5 or SHA) to create the MAC.
The MAC is sent along with the message to the receiver.
Receiver's Side:

The receiver combines the received message with the same secret key 
and computes the MAC.
If the computed MAC matches the received MAC, the message is
 considered authentic and intact.
'''
#MD5
import hashlib

# Create MD5 hash of a message
result = hashlib.md5(b'Ismile')
result1 = hashlib.md5(b'Esmile')

print("MD5 Hash of 'Ismile':", result.digest())
print("MD5 Hash of 'Esmile':", result1.digest())

#SHA1
import hashlib

# Input string to encode
str = input("Enter the value to encode: ")
result = hashlib.sha1(str.encode())

print("SHA1 Hash:", result.hexdigest())
