# Victoria Villasana 86143370
from eliza_decoder import *

def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)  # Shifting up by 3 numbers
        encoded_password += encoded_digit
    return encoded_password

def decode(enc_password):
    decoded_password = ""
    for i in range(0, len(enc_password)):
        num = int(enc_password[i]) - 3
        decoded_password += str(num)
    return decoded_password


def main():
    while True:
        print("\nMenu:")
        print("1. Encode Password")
        print("2. Decode Password")
        print("3. Exit")

        choice = input("Enter menu choice: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            if len(password) != 8 or not password.isdigit():
                print("Error: Password must be an 8-digit integer.")
            else:
                encoded_password = encode(password)
                print("Your password has been encoded and stored")
        elif choice == "2":
            encoded_password = input("Enter the encoded password to decode: ")
            if len(encoded_password) != 8 or not encoded_password.isdigit():
                print("Error: Encoded password must be an 8-digit integer.")
            else:
                decoded_password = decode(encoded_password)
                print(f"Your encoded password is {encoded_password}, and the original password is {decoded_password}))")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
