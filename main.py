from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet instance

message = input("Enter the message: ")

key = Fernet.generate_key()
print(str("Here is your key: ") + str(key))
f = Fernet(key)
token = f.encrypt(message.encode())
print(token)

deToken = f.decrypt(token)
print(deToken)
