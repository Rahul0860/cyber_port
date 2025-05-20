import re

def check_password_strength(password, requirements=None, weak_passwords=None):
    """
    Evaluates the strength of a password against a set of criteria,
    including a check against a list of weak passwords.

    Args:
        password (str): The password to evaluate.
        requirements (dict, optional): A dictionary specifying the password requirements.
            Defaults to:
            {
                "min_length": 8,
                "has_digit": True,
                "has_upper": True,
                "has_lower": True,
                "has_special": True,
            }
        weak_passwords (list, optional): A list of known weak passwords.
            Defaults to an empty list.

    Returns:
        tuple: (strength_level, message, score, color)
            - strength_level (str): "Very Weak", "Weak", "Medium", "Strong", "Excellent"
            - message (str): A detailed explanation of the password strength.
            - score (int): A numerical score representing the password's complexity.
            - color (str): ANSI color code for the strength level.
    """
    if requirements is None:
        requirements = {
            "min_length": 8,
            "has_digit": True,
            "has_upper": True,
            "has_lower": True,
            "has_special": True,
        }

    if weak_passwords is None:
        weak_passwords = []

    score = 0
    messages = []
    
    # Check against weak password list first.
    if password in weak_passwords:
        return "Very Weak", "Password is in the list of known weak passwords", 0, "\033[31m"  # Red

    length_requirement = requirements.get("min_length", 8)  #handles if key does not exist.
    if len(password) < length_requirement:
        messages.append(f"Password must be at least {length_requirement} characters long")
        score -= 1  # Deduct, not add, for failing a requirement.  Higher score is better, so failing is bad.
    else:
        score += 1  # Award points for meeting the requirement
    
    if requirements.get("has_digit", True) and not any(char.isdigit() for char in password):
        messages.append("Password must contain a digit")
        score -= 1
    elif requirements.get("has_digit", True):
        score += 1

    if requirements.get("has_upper", True) and not any(char.isupper() for char in password):
        messages.append("Password must contain an uppercase letter")
        score -= 1
    elif requirements.get("has_upper", True):
        score += 1

    if requirements.get("has_lower", True) and not any(char.islower() for char in password):
        messages.append("Password must contain a lowercase letter")
        score -= 1
    elif requirements.get("has_lower", True):
        score += 1

    if requirements.get("has_special", True) and not re.search(r'[!@#$%^&*()<>?:.;]', password):
        messages.append("Password must contain a special character")
        score -= 1
    elif requirements.get("has_special", True):
        score += 1

    if not messages:
        messages.append("Password meets all requirements")

    # Determine strength level and color
    if score <= 1:  # Adjusted score ranges for new scoring
        strength_level = "Very Weak"
        color = "\033[31m"  # Red
    elif score == 2:
        strength_level = "Weak"
        color = "\033[31m"  # Red
    elif score == 3:
        strength_level = "Medium"
        color = "\033[33m"  # Yellow
    elif score == 4:
        strength_level = "Strong"
        color = "\033[32m"  # Green
    else:
        strength_level = "Excellent"  # Highest possible score is now 5
        color = "\033[32m"  # Green

    return strength_level, ". ".join(messages), score, color


def password_checker():
    """
    Interactive command-line tool to check password strength.
    """
    print("Welcome to the Enhanced Password Strength Checker!")
    
    # Define default requirements.  This can be overridden in the loop.
    default_requirements = {
        "min_length": 8,
        "has_digit": True,
        "has_upper": True,
        "has_lower": True,
        "has_special": True,
    }
    
    # Load the weak password list (SecList example).
    weak_passwords = ["password", "123456", "qwerty", "admin", "guest", "camper", "123456789"]  # Example list
    
    while True:
        try:
            password = input("Enter your password (or type 'exit' to quit): ")
        except EOFError:
            print("\nNo more input. Exiting.")
            break  # Exit the loop

        if password.lower() == "exit":
            print("Thank you for using this tool!")
            break

        # Allow the user to customize the requirements.
        try:
            custom_requirements = input("Enter custom requirements (e.g., min_length=12,has_special=False, or leave blank for default): ")
        except EOFError:
            print("\nNo more input. Exiting.")
            break  # Exit the loop
        
        requirements = default_requirements #start with defaults
        if custom_requirements:
            try:
                # Parse the user input.  Split by comma, then split each part by =
                for part in custom_requirements.split(','):
                    if '=' in part: # Check if the part contains =
                        key, value = part.split('=')
                        key = key.strip()
                        value = value.strip().lower() #handle bools better
                        if key == "min_length":
                            requirements["min_length"] = int(value)
                        elif key == "has_digit":
                            requirements["has_digit"] = value == "true"
                        elif key == "has_upper":
                            requirements["has_upper"] = value == "true"
                        elif key == "has_lower":
                            requirements["has_lower"] = value == "true"
                        elif key == "has_special":
                            requirements["has_special"] = value == "true"
                    #handle other cases
            except ValueError:
                print("Invalid requirements format. Using default requirements.")
                requirements = default_requirements #reset
                
        strength, message, score, color = check_password_strength(password, requirements, weak_passwords)
        print(f"Strength: {color}{strength}\033[0m")  # Print with color, reset after
        print(f"Details: {message}")
        print(f"Score: {score}")  # Display the score

if __name__ == "__main__":
    password_checker()
