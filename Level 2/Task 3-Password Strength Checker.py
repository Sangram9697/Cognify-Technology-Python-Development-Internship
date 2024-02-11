import re

def password_strength(password):
    # Length check
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    
    # Uppercase and lowercase letters check
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return "Weak: Password should contain both uppercase and lowercase letters."
    
    # Digit check
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    
    # Special character check
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password should contain at least one special character."
    
    return "Strong: Password meets the criteria for strength."

# Test the function
password = input("Enter your password: ")
print(password_strength(password))
