# Day 17: Caesar Cipher - Simple Encryption

print("=" * 35)
print("     CAESAR CIPHER")
print("=" * 35)

def encrypt(text, shift):
    """Encrypt text by shifting letters"""
    result = ""
    
    # We loop through each character in the text
    for char in text:
        if char.isalpha():  # Checks if it's a letter
            # We get the ASCII value and shift it
            start = ord('A') if char.isupper() else ord('a')
            new_position = (ord(char) - start + shift) % 26
            result += chr(start + new_position)
        else:
            result += char  # Keeps spaces and punctuation
    return result

def decrypt(text, shift):
    """Decrypt by shifting backwards"""
    return encrypt(text, -shift)  # Just reverses the shift

while True:
    print("\n1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    choice = input("\nChoose (1-3): ")
    
    if choice == "1":
        message = input("Enter message to encrypt: ")
        try:
            shift = int(input("Shift amount (1-25): "))
            if 1 <= shift <= 25:
                encrypted = encrypt(message, shift)
                print(f"\nEncrypted: {encrypted}")
            else:
                print("Shift must be between 1 and 25!")
        except:
            print("Invalid shift amount!")
    
    elif choice == "2":
        message = input("Enter message to decrypt: ")
        try:
            shift = int(input("Shift amount used: "))
            if 1 <= shift <= 25:
                decrypted = decrypt(message, shift)
                print(f"\nDecrypted: {decrypted}")
            else:
                print("Shift must be between 1 and 25!")
        except:
            print("Invalid shift amount!")
    
    elif choice == "3":
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice!")