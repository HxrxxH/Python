def caesar_cipher_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

encrypted_message = input("Enter encrypted message: ")
shift_value = int(input("Enter shift value: "))
print("Decrypted message:", caesar_cipher_decrypt(encrypted_message, shift_value))
