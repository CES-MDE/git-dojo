def substitution_encrypt(text: str, key: str) -> str:
    """
    Encrypts the given text using a substitution cipher with the specified key.

    Args:
        text (str): The text to be encrypted.
        key (str): The substitution key.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += key[ord(char.lower()) - ord('a')].lower()
            else:
                encrypted_text += key[ord(char) - ord('A')]
        else:
            encrypted_text += char
    return encrypted_text

def substitution_decrypt(text: str, key: str) -> str:
    """
    Decrypts the given text using a substitution cipher with the specified key.

    Args:
        text (str): The text to be decrypted.
        key (str): The substitution key.

    Returns:
        str: The decrypted text.
    """
    # Un cryptage par substitution est une technique de cryptographie où chaque lettre dans le texte original est remplacée par une autre lettre selon une règle fixe.
    # TODO : Utilisez la fonction substitution_encrypt pour décrypter le texte chiffré.
    return 

# Vous pouvez tester les fonctions ici
if __name__ == "__main__":
    plaintext = "Joan Elisabeth Lowther Murray Clarke"
    key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    encrypted_text = substitution_encrypt(plaintext, key)
    print("Texte chiffré:", encrypted_text)
    decrypted_text = substitution_decrypt(encrypted_text, key)
    print("Texte déchiffré:", decrypted_text)