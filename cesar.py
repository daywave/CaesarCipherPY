def caesar_decrypt(ciphertext, shift):
    alphabet = "!#$%&()*+,-./:;<>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz{|}éÉáíóúñÑ¿ÁÍÓÚ0123456789"
    result = ''
    for character in ciphertext:
        if character in alphabet:
            index = (alphabet.index(character) - shift) % len(alphabet)
            result += alphabet[index]
        else:
            result += character
    return result

# Example of usage
ciphertext = ""
shift = 88
decrypted_text = caesar_decrypt(ciphertext, shift)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)