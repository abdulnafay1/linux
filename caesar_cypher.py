import sys

def caesar_cipher(message, shift):
    encoded_message = ''
    for char in message.upper():
        if char.isalpha():
            encoded_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encoded_message += encoded_char
    return encoded_message

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 caesar_cipher.py <shift>")
        sys.exit(1)

    try:
        shift = int(sys.argv[1])
        if shift < 0 or shift > 25:
            raise ValueError
    except ValueError:
        print("Shift must be an integer between 0 and 25.")
        sys.exit(1)

    message = input("Enter the message to be encrypted: ")
    encoded_message = caesar_cipher(message, shift)
    print("\nEncoded Message:")
    for i in range(0, len(encoded_message), 5):
        print(encoded_message[i:i+5], end=' ')
    print()
