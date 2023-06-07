# affine cipher

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def find_mod_inverse(num, mod):
    if find_gcd(num, mod) == 1:
        for i in range(1, mod):
            if (num * i) % mod == 1:
                return i
    return None


def encrypt_affine(plain_text, encryption_key):
    a, b = encryption_key
    cipher_text = ""
    for character in plain_text:
        if character.isalpha():
            if character.isupper():
                cipher_text += chr((a * (ord(character) - 65) + b) % 26 + 65)
            else:
                cipher_text += chr((a * (ord(character) - 97) + b) % 26 + 97)
        else:
            cipher_text += character
    return cipher_text


        
def decrypt_affine(encrypted_text, decryption_key):
    a, b = decryption_key
    original_text = ""
    a_inv = find_mod_inverse(a, 26)
    if a_inv is None:
        return "Error: Invalid key. 'a' and 26 must be coprime."
    for character in encrypted_text:
        if character.isalpha():
            if character.isupper():
                original_text += chr((a_inv * (ord(character) - 65 - b)) % 26 + 65)
            else:
                original_text += chr((a_inv * (ord(character) - 97 - b)) % 26 + 97)
        else:
            original_text += character
    return original_text


# Example usage:

input_text = "hey, Google!"
encryption_key = (5, 7)  # 'a' = 5, 'b' = 7
cipher_text = encrypt_affine(input_text, encryption_key)
deciphered_text = decrypt_affine(cipher_text, encryption_key)

print("Input text:", input_text)
print("Encrypted text:", cipher_text)
print("Decrypted text:", deciphered_text)