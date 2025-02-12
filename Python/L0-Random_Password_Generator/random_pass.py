import random
import string

def random_pass():
    length = int(input("Enter password length: "))

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

    char_seq = ""
    if use_upper:
        char_seq += string.ascii_uppercase
    if use_lower:
        char_seq += string.ascii_lowercase
    if use_digits:
        char_seq += string.digits
    if use_symbols:
        char_seq += "!@#$%^&*?/"

    if not char_seq:
        print("You must select at least one character type!")
        return

    password = ''.join(random.choice(char_seq) for _ in range(length))
    print(f"Generated Password: {password}")

random_pass()
