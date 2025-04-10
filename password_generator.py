import random

def main():
    print("Welcome to password generator.", sep="")
    max_length = int(input("Enter max password length: "))
    unwanted_chars = []
    char_entered = ""
    while char_entered != "/q":
        char_entered = input("Enter a character to exclude. Enter '/q' to end unwanted char registration: ")
        unwanted_chars.append(char_entered)
    unwanted_chars.pop(len(unwanted_chars)-1)
    password = generate_pass(max_length, unwanted_chars)

    print(f"Your password is: {password}")

def generate_pass(max_length, unwanted_chars):
    password = ""
    for _ in range (0, max_length):
        current_char=chr(random.randint(33,126))
        while current_char+"" in unwanted_chars:
            current_char=chr(random.randint(33,126))

        password+=current_char

    return password

if __name__ == "__main__":
    main()        