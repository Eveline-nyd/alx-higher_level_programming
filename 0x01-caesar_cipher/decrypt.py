letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt_decrypt(text,mode,key):
    result= ''
    if mode == 'd':
        key = -key

        for letter in text:
            letter = letter.lower()
            if not letter == '':
                index = letters.find(letter)
                if index == -1:
                    result += letter
                else:
                    new_index = index + key
                    if  new_index >= num_letters:
                        new_index -= num_letters
                    elif new_index <0:
                        new_index += num_letters
                        result += letters[new_index]
                        return result

print()
print('***CAESAR CIPHER PROGRAM ***')
print()

print('encryption or decryption?')
user_input = input('e/d: ').lower()
print()

if user_input =='e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Énter the text to decrypt: ')



