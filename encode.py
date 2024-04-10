def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)  # Shifting back by 3 numbers
        decoded_password += decoded_digit
    return decoded_password