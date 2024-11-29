import re

def check_password_strength(password):
    """
    This function checks the strength of the given password based on:
    - Length (minimum 8 characters)
    - Inclusion of at least one uppercase letter
    - Inclusion of at least one lowercase letter
    - Inclusion of at least one digit
    - Inclusion of at least one special character
    """
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        return "Weak: Password is too short, must be at least 8 characters."

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter."

    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return "Weak: Password must contain at least one lowercase letter."

    # Check for at least one digit
    if not re.search(r"[0-9]", password):
        return "Weak: Password must contain at least one digit."

    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must contain at least one special character."

    # If all conditions are met, the password is strong
    return "Strong password!"

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")
