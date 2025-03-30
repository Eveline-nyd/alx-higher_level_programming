#!/usr/bin/env python3
letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ''

    if mode == 'd':  # Decryption mode
        key = -key  

    for letter in text:
        is_upper = letter.isupper()  # Check if letter is uppercase
        letter = letter.lower()  # Convert to lowercase for processing

        if letter in letters:  # Only process letters
            index = letters.find(letter)
            new_index = (index + key) % num_letters  # Wrap around the alphabet
            new_letter = letters[new_index]
            result += new_letter.upper() if is_upper else new_letter  # Preserve case
        else:
            result += letter  # Preserve spaces, punctuation, numbers

    return result  # Return the final result after processing all letters


# Original decrypted paragraph
original_text = """A LONG MESSAGE CONTAINS LOTS OF STATISTICAL CLUES THAT CAN BE USED TO ANALYSE WHAT THE MOST FREQUENT LETTERS ARE, AND EVEN THE MOST COMMON PAIRS OR TRIPLES OF LETTERS CAN HELP TO BREAK THE CODE"""

# Step 1: Encrypt the paragraph (Shift = 5)
encrypted_text = encrypt_decrypt(original_text, 'e', 5)
print("\nEncrypted Text:\n", encrypted_text)

# Step 2: Decrypt the encrypted paragraph (Shift = 5)
decrypted_text = encrypt_decrypt(encrypted_text, 'd', 5)
print("\nDecrypted Text:\n", decrypted_text)

