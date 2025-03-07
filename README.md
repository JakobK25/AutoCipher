# AutoCipher
A Python encryption/decryption tool using the Fernet symmetric encryption method.

## Features
- Encrypt text messages with a secure key
- Decrypt messages using the provided key
- Simple command-line interface

## Installation
### Clone the repository:
~~~
git clone https://github.com/jakobk25/AutoCipher.git
cd AutoCipher-1
~~~

### Create a virtual environment (recommended):
~~~
python -m venv .venv
~~~

### Activate the virtual environment:

Windows: activate
macOS/Linux: source .venv/bin/activate

### Install dependencies:
~~~
pip install -r requirements.txt
~~~

## Usage
Run the program:
~~~
python main.py
~~~

### Encrypting a Message
- Enter encrypt when prompted
- Type the message you want to encrypt
- Save the generated key and encrypted message

### Decrypting a Message
Enter decrypt when prompted
Enter the key that was provided during encryption
Enter the encrypted message
View your decrypted message

### Requirements
Python 3.x
cryptography package

## License
This project is licensed under the MIT License - see the LICENSE file for details.
