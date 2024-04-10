

def decode(enc_password):
    decoded_password = ""
    for i in range(0, len(enc_password)):
        num = int(enc_password[i]) - 3
        decoded_password += str(num)
    return decoded_password