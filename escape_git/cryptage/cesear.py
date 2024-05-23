def caesar_encrypt(text: str, shift: int) -> str:
    """
    Encrypts the given plaintext using the Caesar cipher with the specified shift.

    Args:
        text (str): The text to be encrypted.
        shift (int): The shift value used for encryption.

    Returns:
        str: The encrypted ciphertext.
    """
    ciphertext = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(text: str, shift: int) -> str:
    """
    Decrypts the given ciphertext using the Caesar cipher with the specified shift.

    Args:
        text (str): The text to be decrypted.
        shift (int): The shift value used for decryption.

    Returns:
        str: The decrypted plaintext.
    """
    # Pour rappel, Cesear est une méthode de cryptage par décallage des lettres. 
    # Avec Shift = 2, A devient C et B devient D.
    # Avec Shift = 3, A devient D et B devient E
    # TODO : Utilisez la fonction caesar_encrypt pour décrypter le texte chiffré.
    return 


# Vous pouvez tester les fonctions ici
if __name__ == "__main__":
    texte_à_endécoder = "Elizebeth Smith Friedman"
    shift = 2
    texte_endécoder = caesar_encrypt(texte_à_endécoder, shift)
    print("Texte chiffré:", texte_endécoder)
    texte_décoder = caesar_decrypt(texte_endécoder, shift)
    print("Texte déchiffré:", texte_décoder)


 
import string