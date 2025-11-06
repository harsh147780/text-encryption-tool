def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def caesar_decrypt(cipher_text, shift):
    return caesar_encrypt(cipher_text, -shift)


def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt)? ").upper()
    text = input("Enter your text: ")
    shift = int(input("Enter shift value (1-25): "))

    if choice == 'E':
        encrypted = caesar_encrypt(text, shift)
        print(f"\nEncrypted text: {encrypted}")
    elif choice == 'D':
        decrypted = caesar_decrypt(text, shift)
        print(f"\nDecrypted text: {decrypted}")
    else:
        print("Invalid choice! Please select E or D.")


if __name__ == "__main__":
    main()
