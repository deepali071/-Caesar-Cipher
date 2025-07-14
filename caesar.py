def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Keep other characters unchanged
            result += char

    return result

def main():
    print("=== Caesar Cipher Encryption & Decryption ===")
    
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter E or D.")
        return

    message = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value (e.g. 3): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'e':
        encrypted = caesar_cipher(message, shift, mode='encrypt')
        print("Encrypted Message:", encrypted)
    else:
        decrypted = caesar_cipher(message, shift, mode='decrypt')
        print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()
