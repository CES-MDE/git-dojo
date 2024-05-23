def vigenere_encrypt(text: str, key: str) -> str:
    """
    Encrypts the given plaintext using the Vigenère cipher with the specified key.

    Args:
        plaintext (str): The text to be encrypted.
        key (str): The key used for encryption.

    Returns:
        str: The encrypted ciphertext.
    """
    key = key.upper()
    key_index = 0
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                shift = ord(key[key_index % len(key)]) - ord('A')
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                shift = ord(key[key_index % len(key)]) - ord('A')
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts the given ciphertext using the Vigenère cipher with the specified key.

    Args:
        ciphertext (str): The text to be decrypted.
        key (str): The key used for decryption.

    Returns:
        str: The decrypted plaintext.
    """
    key = key.upper()
    key_index = 0
    decrypted_text = ""  
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                shift = ord(key[key_index % len(key)]) - ord('A')
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                shift = ord(key[key_index % len(key)]) - ord('A')
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

# Vous pouvez tester les fonctions ici
if __name__ == "__main__":
    plaintext = "Hugo Alexander Koch"#
    key = "KEY"
    encrypted_text = vigenere_encrypt(plaintext, key)
    print("Texte chiffré:", encrypted_text)
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Texte déchiffré:", decrypted_text)