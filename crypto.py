import hashlib
import base64
from Crypto.Cipher import AES
import os

def display_intro():
    print("************************************")
    print("*  Welcome to Akash Motkar's Tool  *")
    print("************************************")
    print("\nDisclaimer: This tool is provided as-is. Use it responsibly and at your own risk.\n")

def display_menu():
    print("\nChoose an operation:")
    print("1) Hashing")
    print("2) Encoding")
    print("3) Decoding")
    print("4) Exit")

def hashing(data):
    # Hashing function (e.g., using SHA-256)
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    return hashed_data

def encoding(data):
    # Encoding function (e.g., using base64)
    encoded_data = base64.b64encode(data.encode()).decode()
    return encoded_data

def decoding(data):
    # Decoding function (e.g., using base64)
    decoded_data = base64.b64decode(data.encode()).decode()
    return decoded_data

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

def main():
    display_intro()

    while True:
        display_menu()

        try:
            choice = int(input("Enter the number corresponding to your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            user_input = input("Enter the data to hash: ")
            result = hashing(user_input)
        elif choice == 2:
            user_input = input("Enter the data to encode: ")
            result = encoding(user_input)
        elif choice == 3:
            user_input = input("Enter the data to decode: ")
            result = decoding(user_input)
        elif choice == 4:
            print("Thanks for using Akash Motkar's Tool!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        output_filename = f"output_{choice}.txt"
        save_to_file(result, output_filename)

        print(f"\nResult:\n{result}\n")
        print(f"Result saved to {output_filename}\n")

if __name__ == "__main__":
    main()

