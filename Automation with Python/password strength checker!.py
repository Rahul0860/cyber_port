# Passwod strength checker
import re
# password strength check condition:
#min 8 chars, didgit, uppercase, special char
def check_password_strangth(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 chars"

    if not any(char.isdigit() for char in password):
        return "Weak: password must be contentin a digit"

    if not any(char.isupper() for char in password):
        return "Weak: password must contain an upper letter char"

    if not any(char.islower() for char in password):
        return "Weak: password must contain an lower letter char"

    if not re.search(r'[!@#$%^&*()<>?:.;]' , password):
        return "Medium: password must contain a sepcial char"

    return "strong: your password is secured"

def password_checker():
    print("Welcome to the password stranth checker")

    while True:
        password = input("Enter your password (or type 'exit to quit'): ")

        if password.lower() == 'exit':
            print("Thank you using this tool")
            break

        result = check_password_strangth(password)
        print(result)

# Run the password checker()

if __name__ == "__main__":
    password_checker()