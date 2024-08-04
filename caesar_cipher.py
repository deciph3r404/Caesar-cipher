def encrypt(text):
    shift = 3  # Fixed shift value
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text):
    shift = 3  # Fixed shift value
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Do you want to encrypt or decrypt the text? (e/d): ").lower()
    if choice not in ('e', 'd'):
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        return

    text = input("Enter text to encrypt/decrypt: ")

    if choice == 'e':
        result_text = encrypt(text)
        print("\nOriginal Text:", text)
        print("Encrypted Text:", result_text)
    else:
        result_text = decrypt(text)
        print("\nOriginal Text:", text)
        print("Decrypted Text:", result_text)

if __name__ == "__main__":
    main()
