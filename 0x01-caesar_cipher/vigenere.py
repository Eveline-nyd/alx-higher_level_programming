#!/usr/bin/env python3
def vigenere_encrypt(plaintext, keyword):
    """
    Encrypts plaintext using the Vigenère cipher with the given keyword.
    Preserves case and non-alphabetic characters.
    """
    ciphertext = []
    keyword = keyword.upper()
    keyword_length = len(keyword)
    keyword_index = 0

    for char in plaintext:
        if char.isalpha():
            # Determine the shift value from the keyword
            shift = ord(keyword[keyword_index % keyword_length]) - ord('A')

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # Apply the Vigenère shift
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext.append(encrypted_char)

            # Move to next keyword character
            keyword_index += 1
        else:
            # Keep non-alphabetic characters unchanged
            ciphertext.append(char)

    return ''.join(ciphertext)


def vigenere_decrypt(ciphertext, keyword):
    """
    Decrypts ciphertext using the Vigenère cipher with the given keyword.
    Preserves case and non-alphabetic characters.
    """
    plaintext = []
    keyword = keyword.upper()
    keyword_length = len(keyword)
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():
            # Determine the shift value from the keyword
            shift = ord(keyword[keyword_index % keyword_length]) - ord('A')

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # Apply the reverse Vigenère shift
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext.append(decrypted_char)

            # Move to next keyword character
            keyword_index += 1
        else:
            # Keep non-alphabetic characters unchanged
            plaintext.append(char)

    return ''.join(plaintext)


# Example usage
if __name__ == "__main__":
    plaintext = "Telecommunication and Information Engineering"
    keyword = "Mapangale"

    encrypted = vigenere_encrypt(plaintext, keyword)
    decrypted = vigenere_decrypt(encrypted, keyword)

    print(f"Original:  {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
