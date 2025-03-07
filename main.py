from cryptography.fernet import Fernet
import os

os.system('cls')

running = True

while running == True:

    print("Welcome to the encryption program!")
    choice = input("Enter 'encrypt' or 'decrypt': ")

    if choice == "encrypt":
        message = input("Enter the message you would like to encrypt: ")
        os.system('cls')

        key = Fernet.generate_key()
        print(str("Here is your key: ") + str(key))
        print()

        f = Fernet(key)
        token = f.encrypt(message.encode())

        print("Here is your encrypted message: ")
        print(token)
    if   choice == "decrypt":
        key = input("Enter your key: ")
        token = input("Enter your encrypted message: ")

        os.system('cls')
        f = Fernet(key)
        message = f.decrypt(token)

        print("Here is your decrypted message:")
        print(message.decode())

    break 


        
    

