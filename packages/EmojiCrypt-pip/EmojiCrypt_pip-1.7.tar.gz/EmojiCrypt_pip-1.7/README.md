# EmojiCrypt_pip

EmojiCrypt_pip is a Python package designed to provide a unique and fun way to encrypt and decrypt messages using emojis. This approach not only makes the encryption process more interesting, but also adds a layer of abstraction to the original text, making the encrypted message less noticeable at first glance.

## Installation

You can install EmojiCrypt_pip directly from PyPI:

```bash
pip install EmojiCrypt_pip
```
Make sure you have Python and pip already installed on your system to be able to run this command without problems.

## Usage

EmojiCrypt_pip is extremely easy to use with only two main functions: encrypt to encrypt messages and decrypt to decrypt messages previously encrypted with this package.

### Encrypt a message
To encrypt a message, simply import the encrypt function and pass it the message you want to encrypt as an argument.

```python
from EmojiCrypt_pip import encrypt

encrypted_message = encrypt("Your message here")
print(encrypted_message)
```
This will convert your message into a string of emojis representing the ciphertext.


### Decrypting a message
To decrypt a message that was encrypted with EmojiCrypt_pip, use the decrypt function in a similar way.

```python
from EmojiCrypt_pip import decrypt

decrypted_message = decrypt(decrypted_message)
print(decrypted_message)
```

Be sure to replace decrypted_message with the emoji string you received when encrypting your original message. This 

Translated with DeepL.com (free version)
