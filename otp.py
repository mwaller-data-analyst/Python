#This code creates secure one-time passwords.

import secrets
import string

def generate_otp(length=6, numeric_only=False):
    characters = string.digits if numeric_only else string.digits + string.ascii_letters + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

choice = input("Generate numeric OTP only? (y/n): ").lower() == 'y'
otp = generate_otp(8, numeric_only=choice)
print("Generated OTP:", otp)
