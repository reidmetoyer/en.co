#welcome to en.co, a basic encryption/decryption website to mess around with your friends
#in this program, we use a simple caesar cipher to encrypt and decrypt basic messages

def cipher(message, mode, key):
    if mode == 2:
        key = 0-key

    ledger = "abcdefghijklmnopqrstuvwxyz 1234567890"

    crypt_msg = ""

    for i, char in enumerate(message):
        if char.lower() in ledger:
            position = ledger.index(char.lower())
            new_position = (position + key) % len(ledger)
            crypt_char = ledger[new_position]
            crypt_msg += crypt_char
        else:
            crypt_msg += char  # Keep non-alphanumeric characters as is

    return crypt_msg


# Test the function
if __name__ == "__main__":
    msg = "3t51mfiizu5jqrjwt5gqfpjrjwt"
    mode = 2
    key = 5
    result = cipher(msg, mode, key)
    print(result)



