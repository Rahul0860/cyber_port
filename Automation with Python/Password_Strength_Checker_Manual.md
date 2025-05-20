# Password Strength Checker Manual 
[Code](https://github.com/Rahul0860/cyber_port/blob/main/Automation%20with%20Python/password_checker_2.py)


## Introduction

This document provides a comprehensive guide to the Password Strength Checker tool, a Python script designed to evaluate the security of passwords. It outlines the tool's features, usage, and underlying principles.

## Features

The Password Strength Checker offers a range of features to help users assess password security:

* **Password Strength Evaluation:** The core functionality of this tool is to analyze a given password and determine its strength based on a set of criteria.
* **Customizable Requirements:** Users can define specific password requirements, including:
    * Minimum length
    * Presence of digits
    * Presence of uppercase letters
    * Presence of lowercase letters
    * Presence of special characters
* **Check Against Weak Password List:** The tool can check passwords against a predefined list of known weak passwords (e.g., from the SecList database).
* **Detailed Feedback:** The tool provides informative messages indicating the password's strength and the reasons for its classification.
* **Scoring System:** A numerical score represents the password's complexity, offering a quantitative measure of its strength.
* **Color-Coded Output:** The tool uses ANSI escape codes to display the password strength in color-coded format, enhancing readability.
* **User-Friendly Interface:** The tool provides an interactive command-line interface for ease of use.

## Code Description

The Password Strength Checker is implemented in Python and consists of the following functions:

### `check_password_strength(password, requirements=None, weak_passwords=None)`

This function evaluates the strength of a password based on the provided criteria and weak password list.

**Parameters:**

* `password` (str): The password to evaluate.
* `requirements` (dict, optional): A dictionary specifying the password requirements. Defaults to:

    ```python
    {
        "min_length": 8,
        "has_digit": True,
        "has_upper": True,
        "has_lower": True,
        "has_special": True,
    }
    ```
* `weak_passwords` (list, optional): A list of known weak passwords. Defaults to an empty list.

**Returns:**

* tuple: (strength\_level, message, score, color)
    * `strength_level` (str): "Very Weak", "Weak", "Medium", "Strong", "Excellent"
    * `message` (str): A detailed explanation of the password strength.
    * `score` (int): A numerical score representing the password's complexity.
    * `color` (str): ANSI color code for the strength level.

### `password_checker()`

This function provides an interactive command-line interface for checking password strength.

**Features:**

* Prompts the user to enter a password.
* Allows the user to customize the password requirements.
* Checks the password against the specified requirements and a list of weak passwords.
* Displays the password strength, feedback message, and score.
* Exits gracefully when the user enters "exit".

## Usage

1.  **Installation:** Ensure you have Python installed on your system.
2.  **Save the code:** Save the provided Python code as a `.py` file (e.g., `password_checker.py`).
3.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and run the script using the command `python password_checker.py`.
4.  **Enter a password:** The script will prompt you to enter a password. Type the password you want to check and press Enter.
5.  **View the results:** The script will display the password strength, a detailed explanation, and a numerical score.
6.  **Customize requirements (optional):** The script will prompt you to enter custom requirements. Enter requirements in the format `key=value`, separated by commas (e.g., `min_length=12,has_special=False`). If you leave this blank, the default requirements will be used.
7.  **Exit:** To exit the program, type "exit" when prompted for a password.

## Example

Welcome to the Enhanced Password Strength Checker!Enter your password (or type 'exit' to quit): myPassword123!Enter custom requirements (e.g., min_length=12,has_special=False, or leave blank for default):Strength: \033[32mStrong\033[0mDetails: Password meets all requirementsScore: 4Enter your password (or type 'exit' to quit): weakpassEnter custom requirements (e.g., min_length=12,has_special=False, or leave blank for default):Strength: \033[31mVery Weak\033[0mDetails: Password is in the list of known weak passwordsScore: 0Enter your password (or type 'exit' to quit): exitThank you for using this tool!
## Potential Use Cases

* **Password Policy Enforcement:** This tool can be used to enforce password policies in organizations or applications.
* **User Education:** Users can use this tool to check the strength of their passwords and learn how to create more secure ones.
* **Security Audits:** Security professionals can use this tool to assess the password security of systems or users.
* **Application Development:** Developers can integrate this tool into their applications to ensure that users create strong passwords.
