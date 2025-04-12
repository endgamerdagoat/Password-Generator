import random
import string
import argparse
import pyperclip

def generate_password(length, unwanted_chars, use_letters, use_digits, use_symbols):
    char_pool = ""

    if use_letters:
        char_pool += string.ascii_letters
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation


    allowed_chars = [c for c in char_pool if c not in unwanted_chars]

    if not allowed_chars:
        raise ValueError("No characters left to generate password after exclusions.")

    return ''.join(random.choices(allowed_chars, k=length))

def interactive_mode():
    print("Welcome to the password generator (interactive mode).")


    while True:
        try:
            length = int(input("Enter max password length: "))
            break
        except ValueError:
            print("Please enter a valid number.")


    print("Include the following in your password? (y/n)")
    use_letters = input("Letters (A-Z, a-z): ").lower().startswith('y')
    use_digits = input("Digits (0-9): ").lower().startswith('y')
    use_symbols = input("Symbols (!@#$ etc): ").lower().startswith('y')

    if not any([use_letters, use_digits, use_symbols]):
        print("At least one character type must be included.")
        return


    unwanted_chars = set()
    while True:
        char = input("Enter a character to exclude. Enter '/q' to finish: ")
        if char == "/q":
            break
        if len(char) != 1:
            print("Please enter only one character at a time.")
            continue
        unwanted_chars.add(char)

    try:
        password = generate_password(length, unwanted_chars, use_letters, use_digits, use_symbols)
        print(f"Your password is: {password}")

        copy = input("Copy password to clipboard? (y/n): ").lower().startswith('y')
        if copy:
            pyperclip.copy(password)
            print("Password copied to clipboard!")
    except ValueError as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.",
                                     epilog="If you do not pass any arguments, " \
                                     "the script will run in interactive mode"
                                     )
    parser.add_argument('--length', type=int, help='Length of the password')
    parser.add_argument('--exclude', nargs='*', default=[], help='Characters to exclude (e.g. --exclude a b c)')
    parser.add_argument('--letters', action='store_true', help='Include letters (A-Z, a-z)')
    parser.add_argument('--digits', action='store_true', help='Include digits (0-9)')
    parser.add_argument('--symbols', action='store_true', help='Include symbols (!@#$ etc)')
    parser.add_argument('--copy', action='store_true', help='Copy password to clipboard')

    args = parser.parse_args()

    if args.length:
        use_letters = args.letters
        use_digits = args.digits
        use_symbols = args.symbols

        if not (use_letters or use_digits or use_symbols):
            use_letters = use_digits = use_symbols = True

        try:
            password = generate_password(args.length, set(args.exclude), use_letters, use_digits, use_symbols)
            print(f"Your password is: {password}")
            if args.copy:
                pyperclip.copy(password)
                print("Password copied to clipboard!")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
